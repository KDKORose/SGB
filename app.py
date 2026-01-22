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
        self._shutting_down = False

    async def startup(self):
        self.mongo.connect()
        self.minecraft.start()

    async def shutdown(self):
        if self._shutting_down:
            return
        
        print("Shutting down bot...")

        # MC
        try:
            if self.minecraft:
                await self.minecraft.stop()
                print("Minecraft bot disconnected")
        except Exception as e:
            print("Minecraft shutdown error:", e)

        # Mongo
        try:
            if self.mongo and self.mongo.client:
                self.mongo.client.close()
                print("MongoDB connection closed")
        except Exception as e:
            print("Mongo shutdown error:", e)

        # Discord
        try:
            await self.discord.close()
            print("Discord bot closed")
        except Exception as e:
            print("Discord shutdown error:", e)

    async def run(self):
        # Start all services
        await self.startup()

        try:
            # Run Discord bot (blocks until stopped)
            await self.discord.start(os.getenv("DISCORD_TOKEN"))
        finally:
            # Always shutdown
            await self.shutdown()

