from javascript import require, On, Once, AsyncTask, once, off

mineflayer = require("mineflayer")

class MCBot:
    def __init__(self, username: str):
        self.username = username
        self.bot = None

    async def start(self):
        self.bot = mineflayer.createBot({
            "host": "mc.hypixel.net",
            "username": self.username,
            "auth": "microsoft"
        })

        await once(self.bot, "login")
        print(f"Logged in to hypixel as {self.username}")

    async def stop(self):
        if self.bot:
            self.bot.quit()
    