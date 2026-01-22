import discord
from dotenv import load_dotenv
import os
from discord.ext import commands

load_dotenv()
intents = discord.Intents.default()
client = commands.Bot(command_prefix=os.getenv("BOT_PREFIX"), intents=intents)
tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("Obtaining Guild ID...")

    GUILD_ID = int(os.getenv("GUILD_ID"))
    await load_all_cogs()
    print(f"Obtained Guild ID. {GUILD_ID}")

    print("Local commands:")
    for cmd in tree.walk_commands():
        print("-", cmd.name)

    tree.copy_global_to(guild=discord.Object(id=GUILD_ID))
    synced = await tree.sync(guild=discord.Object(id=GUILD_ID))
    print(f"Synced {len(synced)} commands to guild {GUILD_ID}")


async def load_all_cogs():
    cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")
    for filename in os.listdir(cogs_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            ext_name = f"cogs.{filename[:-3]}"
            try:
                await client.load_extension(ext_name)
                print(f"Loaded cog: {ext_name}")
            except Exception as e:
                print(f"Failed to load {ext_name}: {e}")

client.run(os.getenv("DISCORD_TOKEN"))