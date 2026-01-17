from dotenv import load_dotenv
import discord
from discord.ext import commands
import os

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")
MC_PASS = os.getenv("MC_PASS")
BOT_PREFIX = os.getenv("BOT_PREFIX", "!")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

#if __name__ == "__main__":
    #for file in os.listdir("./cogs"):
        #if file.endswith(".py"):
            #bot.load_extension(f"cogs.{file[:-3]}")

@bot.event
async def on_ready():
    assert bot is not None

    print(f"Logged in as {bot.user}")

@commands.command(name = "test")
async def test(ctx):
    await ctx.send("Hi")

bot.run(DISCORD_TOKEN)

# test1