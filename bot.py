import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

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

client.run('token here')