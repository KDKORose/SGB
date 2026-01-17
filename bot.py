import json
import discord
from discord.ext import commands
import os

HKEY = ""
AUTHKEY = ""
DESCRIPTION = ""

with open("config.json") as config:
    data = json.load(config)
    HKEY = data["hkey"]
    AUTHKEY = data["authkey"]
    DESCRIPTION = data["description"]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="s!",description=DESCRIPTION ,intents=intents)

if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            bot.load_extension(f"cogs.{file[:-3]}")

@bot.event
async def on_ready():
    assert bot is not None

    print(f"Logged in as {bot.user}")

@commands.command(name = "test")
async def test(ctx):
    await ctx.send("Hi")

bot.run(AUTHKEY)