import discord
from sys import argv 

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Returns the string to ping the author of a message.
def ping_author(message):
    return "<@"+str(message.author.id)+">"

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# $Echo: Repeat the message sent by the user.
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$echo'):
        await message.channel.send(message.content[5:])

# If a message is edited, log the initial message to the same channel.
@client.event
async def on_message_edit(before, after):
    if before.author == client.user:
        return

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

if len(argv) != 2:
    print("error: inappropriate amount of arguments")
else:
    client.run(f'{argv[1]}')