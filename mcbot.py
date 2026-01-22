from javascript import require, On, Once, AsyncTask, once, off

mineflayer = require("mineflayer")

class MCBot:
    def __init__(self, username: str):
        self.username = username
        self.bot = None

    def start(self):
        self.bot = mineflayer.createBot({
            "host": "mc.hypixel.net",
            "username": self.username,
            "version": "1.8.9",
            "auth": "microsoft"
        })

        once(self.bot, "login")
        print(f"Logged in to hypixel as {self.username}")

    async def stop(self):
        if self.bot:
            self.bot.quit()

    async def stop(self):
        if self.bot:
            self.bot.quit()
            self.bot = None
    

if __name__ == "__main__":
    mcbot = MCBot("ScandalBot")
    mcbot.start()