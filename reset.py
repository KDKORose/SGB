import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

if not DISCORD_TOKEN or not GUILD_ID:
    raise ValueError("DISCORD_TOKEN and GUILD_ID must be set in .env")

class CommandResetBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.none())  # no events needed

    async def setup_hook(self):
        guild = discord.Object(id=GUILD_ID)
        print("Clearing all slash commands in guild:", GUILD_ID)

        # Remove all guild commands
        self.tree.clear_commands(guild=guild)
        await self.tree.sync(guild=guild)
        print("All guild commands cleared and resynced.")

        await self.close()

async def main():
    await bot.start(DISCORD_TOKEN)

if __name__ == "__main__":
    bot = CommandResetBot()
    asyncio.run(main())
