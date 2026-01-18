from dotenv import load_dotenv
import discord
from discord.ext import commands
import os
from app import BotApp

load_dotenv()

class DCBot(commands.Bot):
    def __init__(self, app: BotApp):

        self.HYPIXEL_KEY = os.getenv("HYPIXEL_KEY")
        self.DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
        self.BOT_PREFIX = os.getenv("BOT_PREFIX")

        super.__init__(command_prefix=self.BOT_PREFIX, intents=discord.Intents.all())
        self.app = app # Access other services
    
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')