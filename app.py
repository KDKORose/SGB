from dcbot import DCBot
from mongoservice import MongoService
from mcbot import MCBot
from dotenv import load_dotenv
import os

load_dotenv()

class BotApp:
    def __init__(self):
        self.mongo = MongoService()
        self.minecraft = MCBot("ScandalBot")
        self.discord = DCBot(self)

    async def startup(self):
        self.mongo.connect()
        self.minecraft.start()

    async def shutdown(self):
        await self.discord.close()
        await self.minecraft.stop()
        self.mongo.close()

    async def run(self):
        # Start all services
        await self.startup()

        try:
            # Run Discord bot (blocks until stopped)
            await self.discord.start(os.getenv("DISCORD_TOKEN"))
        finally:
            # Always shutdown
            await self.shutdown()

