from dcbot import DCBot
from mongoservice import MongoService

class BotApp:
    def __init__(self):
        self.mongo = MongoService()
        self.discord = DCBot(self)

    async def startup(self):
        self.mongo.connect()
        await self.minecraft.start()

    async def shutdown(self):
        await self.discord.close()
        await self.minecraft.stop()
        self.mongo.close()

