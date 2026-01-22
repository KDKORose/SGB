from discord.ext import commands
import os
from discord import Object

class Dev(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.hybrid_command(name="sync", description="Sync bot commands.")
    @commands.has_role(int(os.getenv("DEVELOPER_ROLE_ID")))
    async def sync(self):
        GUILD_ID = int(os.getenv("GUILD_ID"))

        print("Local commands:")
        for cmd in self.bot.tree.walk_commands():
            print("-", cmd.name)

        self.bot.tree.copy_global_to(guild=Object(id=GUILD_ID))
        synced = await self.bot.tree.sync(guild=Object(id=GUILD_ID))
        print(f"Synced {len(synced)} commands to guild {GUILD_ID}")

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