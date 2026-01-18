from dcbot import DCBot
from mongoservice import MongoService
from mcbot import MCBot

class BotApp:
    def __init__(self):
        self.mongo = MongoService()
        self.minecraft = MCBot("ScandalBot")
        self.discord = DCBot(self)

    async def startup(self):
        self.mongo.connect()
        await self.minecraft.start()

    async def shutdown(self):
        await self.discord.close()
        await self.minecraft.stop()
        self.mongo.close()

