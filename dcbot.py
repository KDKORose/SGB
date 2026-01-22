import discord
from discord.ext import commands
import os

class DCBot(commands.Bot):
    def __init__(self, app):

        self.HYPIXEL_KEY = os.getenv("HYPIXEL_KEY")
        self.DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
        self.BOT_PREFIX = os.getenv("BOT_PREFIX")
        self.DEVELOPER_ROLE_ID = os.getenv("DEVELOPER_ROLE_ID")

        super().__init__(command_prefix=self.BOT_PREFIX, intents=discord.Intents.all())
        self.app = app # Access other services

    async def setup_hook(self):
        # Sync slash commands
        GUILD_ID = int(os.getenv("GUILD_ID"))
        await self.load_all_cogs()

        print("Local commands:")
        for cmd in self.tree.walk_commands():
            print("-", cmd.name)

        self.tree.copy_global_to(guild=discord.Object(id=GUILD_ID))
        synced = await self.tree.sync(guild=discord.Object(id=GUILD_ID))
        print(f"Synced {len(synced)} commands to guild {GUILD_ID}")

    async def load_all_cogs(self):
        cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")
        for filename in os.listdir(cogs_dir):
            if filename.endswith(".py") and not filename.startswith("__"):
                ext_name = f"cogs.{filename[:-3]}"
                try:
                    await self.load_extension(ext_name)
                    print(f"Loaded cog: {ext_name}")
                except Exception as e:
                    print(f"Failed to load {ext_name}: {e}")

    async def reload_cogs(self):
        for ext in list(self.extensions):
            await self.reload_extension(ext)
            print(f"Reloaded cog: {ext}")
    
    async def on_command_error(self, ctx, exception):
        if isinstance(exception, commands.MissingPermissions):
            await ctx.send("You are lacking to required permissions to execute this command!")
        elif isinstance(exception, commands.BotMissingPermissions):
            missing_perms = ", ".join(exception.missing_permissions).replace("_", " ")
            await ctx.send("The bot is missing the required permissions to run this command: `{missing_perms}`.")
        elif isinstance(exception, commands.MissingAnyRole):
            missing_roles = ", ".join(exception.missing_roles)
            await ctx.send(f"You are missing at least one of the required roles: `{missing_roles}`.")
        else:
            await ctx.send(f"An unexpected error occurred: {exception}")
    
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')