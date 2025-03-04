import discord
from discord.ext import commands

class PingPongCog(commands.cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        
        if message.content.startswith("$ping"):
            await message.channel.send("pong!")

async def setup(bot):
    await bot.add_cog(PingPongCog(bot))

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Store the bot instance and any other attributes you need
    
    # Commands use this decorator
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Pong!")
    
    # Event listeners use this decorator
    @commands.Cog.listener()
    async def on_message(self, message):
        # Do something with messages
        pass

# This function is required for loading the cog
async def setup(bot):
    await bot.add_cog(MyCog(bot))