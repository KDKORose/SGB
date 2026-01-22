from discord.ext import commands
import os

class Dev(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.hybrid_command(name="stop", description="Stop the bot.")
    @commands.has_role(int(os.getenv("DEVELOPER_ROLE_ID")))
    async def stop(self, ctx):
        print("Stop command called!")
        message = await ctx.send(f"Stopping bot...")
        await self.bot.app.shutdown(message)
    
    @commands.hybrid_command(name="ping",  description="Ping the bot!")
    async def ping(self, ctx):
        print("Ping command called!")
        await ctx.send(f"Pong! Latency of {round(self.bot.latency * 1000)} ms")
    
async def setup(bot: commands.Bot):
    await bot.add_cog(Dev(bot))