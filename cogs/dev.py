from discord.ext import commands

class Dev(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.hybrid_command(name="ping",  description="Ping the bot!")
    async def ping(self, ctx):
        print("Ping command called!")
        await ctx.send(f"Pong! Latency of {self.bot.latency()}.\n Note: Prefix Command!")
    
async def setup(bot: commands.Bot):
    await bot.add_cog(Dev(bot))