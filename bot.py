import discord
from sys import argv 
from random import randint
import re

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Returns the string to ping the author of a message.
def ping_author(message):
    return "<@"+str(message.author.id)+">"

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

# If a message is edited, log the initial message to the same channel.
@client.event
async def on_message_edit(before, after):
    if before.author == client.user:
        return
    # Prevent this from firing when discord errorneously registers pins/embeds as an edit.
    if before.content != after.content:
        # Remove backticks to prevent formatting issues. Doesn't account for escaped backticks.
        stripped_message = before.content.replace("`", "")
        await before.channel.send(ping_author(before) + " just edited their message! Previous Message: ```"+stripped_message+"```")

# If a message gets deleted, log the deleted message to the same channel.
@client.event
async def on_message_delete(message):
    # Remove backticks to prevent formatting issues. Doesn't account for escaped backticks.
    stripped_message = message.content.replace("`", "")
    await message.channel.send(ping_author(message) + " just had a message deleted! Previous Message: ```"+stripped_message+"```")
 
@client.event
async def on_message(message):
    bot_is_author = message.author == client.user

    # $Hello: Respond to the message with 'Hello!'.
    if message.content.startswith('$hello') and not bot_is_author:
        await message.channel.send('Hello!')
    # $Echo: Repeat the message sent by the user.
    elif message.content.startswith('$echo') and not bot_is_author:
        await message.channel.send(message.content[5:])
    # $Roll: Take a number x as input. Output a random number between 1 and x, inclusive.
    elif message.content.startswith('$roll') and not bot_is_author:
        roll_num = re.search('[0-9]+', message.content)
        if not roll_num or roll_num < 1:
            await message.channel.send('No positive integer found in message!')
            return
        await message.channel.send('Rolled a ' + str(randint(1, roll_num)) + '!')
    else:
        on_message_voice(message)

if len(argv) != 2:
    print("error: inappropriate amount of arguments")
else:
    client.run(f'{argv[1]}')

print("testing jenkins")
