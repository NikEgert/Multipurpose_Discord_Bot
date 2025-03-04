import discord
from sys import argv 
from random import randint
import re
import asyncio
import datetime
from datetime import timezone


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
# Bot = 1326366953941499954, Test = 1327533449803726930
bot_ids = {1326366953941499954, 1327533449803726930}


# Returns the string to ping the author of a message.
def ping_author(message):
    return "<@"+str(message.author.id)+">"

# TODO: Function to send a message with mentions, without pinging.
async def send_message_silent_ping(message, mention):
    # Idea: Regex to replace specific calls of {ping_author()} with ...
    # Send that, then edit to original message.
    pass

async def on_message_voice(message):
    if message.author == client.user:
        return
    if message.content.startswith('$play'):
        if message.author.voice:
            channel = message.author.voice.channel
            # Connect the bot to the channel
            await channel.connect()
            await message.channel.send(f"Joined {channel.name}!")
            await message.channel.send(f"In guild {channel.guild}")
        else:
            await message.channel.send("You need to be in a voice channel for me to join.")

    if message.content.startswith('$stop'):
        if message.author.voice:
            if message.guild.voice_client:
                await message.channel.send(f"Leaving vc :(")
                await message.guild.voice_client.disconnect()
        else:
            await message.channel.send(f"youre not even in any vc bruh")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(f'ID: {client.user.id}')

# If a message is edited, log the initial message to the log channel.
@client.event
async def on_message_edit(before, after):
    if before.author.id in bot_ids:
        return
    # Prevent this from firing when discord errorneously registers pins/embeds as an edit.
    if before.content == after.content:
        return
    # Remove backticks to prevent formatting issues. Doesn't account for escaped backticks.
    log_channel = client.get_channel(1331540560036761673)
    stripped_before = before.content.replace("`", "")
    stripped_after = after.content.replace("`", "")
    # If the log channel doesn't exist, reply in the same channel and output a warning.
    if log_channel is None:
        await before.channel.send(f"Warning: Log Channel Not Found.\n"
            f"{ping_author(before)} just edited their message! Previous Message: ```{stripped_before}```")
    # Output edit to log channel. User mention is edited in to avoid pinging them.
    else:
        edit_message = await log_channel.send(f"@{before.author.nick} just edited their message!"
            f"```{stripped_before}``````{stripped_after}```")
        await edit_message.edit(content=f"{ping_author(before)} just edited their message!"""
            f"```{stripped_before}``````{stripped_after}```")

# If a message gets deleted, log the deleted message to the log channel.
@client.event
async def on_message_delete(message):
    # Remove backticks to prevent formatting issues. Doesn't account for escaped backticks.
    log_channel = client.get_channel(1331540560036761673)
    stripped_message = message.content.replace("`", "")
    # If the log channel doesn't exist, reply in the same channel and output a warning.
    if log_channel is None:
        await message.channel.send(f"Warning: Log Channel Not Found.\n"
            f"{ping_author(message)} just had a message deleted! Previous Message: ```{stripped_message}```")
    # If the deleted 
    # Output deletion to log channel. User mention is edited in to avoid pinging them.
    else:
        edit_message = await log_channel.send(f"@{message.author.nick} just had a message deleted!```{stripped_message}```")
        await edit_message.edit(content=f"{ping_author(message)} just had a message deleted!```{stripped_message}```")
 
@client.event
async def on_message(message):
    bot_is_author = message.author == client.user

    # $Hello: Respond to the message with 'Hello!'.
    if message.content.startswith('$hello') and not bot_is_author:
        await message.channel.send('Hello!')
    # $Echo: Repeat the message sent by the user.
    elif message.content.startswith('$echo') and not bot_is_author:
        await message.channel.send(message.content[5:])
        print(message.content)
    # $Time: Prints out the current, time, date, and day, in UTC, right now.
    elif message.content.startswith('$time') and not bot_is_author:
        dt = datetime.datetime.now(timezone.utc)
        time = dt.strftime("%I:%M %p").lstrip("0")
        date = dt.strftime("%d %B, %Y").strip("0")
        offset = dt.strftime("GMT%z")
        day = dt.strftime("%A")
        await message.channel.send(f"# {time}      |      {date} at {offset}.\nToday is a {day}.")
    # $Roll: Take a number x as input. Output a random number between 1 and x, inclusive.
    elif message.content.startswith('$roll') and not bot_is_author:
        match = re.search('[0-9]+', message.content)
        if not match:
            await message.channel.send("No number input!")
            return
        sides = int(match.group())
        match = re.search('d[0-9]+', message.content)
        #if no 'd' in input, execute non-DND roll
        if not match:
            await message.channel.send(f"Rolled {randint(1, sides)}!")
            return
        match = re.search('[0-9]+', match.group())
        sides = int(match.group())
        match = re.search('[0-9]+d', message.content)
        if match:
            match = re.search('[0-9]+', match.group())
            roll_num = int(match.group())
        else:
            roll_num = 1
        #execute dnd roll. Roll dice of 'sides' sides, 'roll_num' times
        accum = 0
        dice_output = ""
        for i in range(roll_num):
            roll = randint(1, sides)
            accum += roll
            dice_output += str(roll)
            dice_output += " "
        try:
            await message.channel.send(f"{dice_output}\nRolled {accum}!")
        except:
            await message.channel.send(f"String too long to send ;)\nRolled {accum}!")
    elif message.content.startswith('$try') and not bot_is_author:
        this_message = await message.channel.send("3")
        await asyncio.sleep(1)
        await this_message.edit(content="2")
        await asyncio.sleep(1)
        await this_message.edit(content="1")
        await asyncio.sleep(1)
        await this_message.edit(content="Fire!")
    else:
        await on_message_voice(message)

if len(argv) != 2:
    print("error: inappropriate amount of arguments")
else:
    client.run(f'{argv[1]}')

print("testing jenkins")
