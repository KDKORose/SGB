from dotenv import load_dotenv
import discord
from discord.ext import commands
import os

load_dotenv()

class DCBot(commands.Bot):
    def __init__(self, app):

        self.HYPIXEL_KEY = os.getenv("HYPIXEL_KEY")
        self.DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
        self.BOT_PREFIX = os.getenv("BOT_PREFIX")

        super().__init__(command_prefix=self.BOT_PREFIX, intents=discord.Intents.all())
        self.app = app # Access other services

    async def setup_hook(self):
        # Sync slash commands
        GUILD_ID = int(os.getenv("GUILD_ID"))
        await self.load_all_cogs()
        await self.tree.sync(guild=discord.Object(id=GUILD_ID))
        print("Synced commands:", self.tree.get_commands(guild=discord.Object(id=GUILD_ID)))

    async def load_all_cogs(self):
        cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")
        for filename in os.listdir(cogs_dir):
            if filename.endswith(".py") and not filename.startswith("__"):
                ext_name = f"cogs.{filename[:-3]}"
                try:
                    await self.load_extension(ext_name)
                    print(f"Loaded cog: {ext_name}")
                except Exception as e:
                    print(f"Failed to load {ext_name}: {e}")

    async def reload_cogs(self):
        for ext in list(self.extensions):
            await self.reload_extension(ext)
            print(f"Reloaded cog: {ext}")
    
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')