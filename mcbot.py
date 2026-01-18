from javascript import require, On, Once, AsyncTask, once, off

mineflayer = require("mineflayer")

username = "ScandalBot"
bot = mineflayer.createBot({
        "host": "mc.hypixel.net",
        "port": "25565",
        "username": username,
        "auth": "microsoft"})

once(bot, "login")
print(f"Logged in to hypixel as {username}")