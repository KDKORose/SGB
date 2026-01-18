from discord.ext import commands
import discord

class Dev(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.hybrid_command(name="ping")
    async def ping(self, ctx: commands.Context):
        if isinstance(ctx, discord.Interaction):
            await ctx.send(f"Pong! Latency of {self.bot.latency()}.\nNote: Slash Command!")
        await ctx.send(f"Pong! Latency of {self.bot.latency()}.\n Note: Prefix Command!")
    
async def setup(bot: commands.Bot):
    await bot.add_cog(Dev(bot))