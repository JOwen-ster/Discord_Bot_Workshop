import discord
from discord.ext import commands
from discord import app_commands

import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Set all intents for discord bot
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Set bot prefix as bash since we like the terminal
client = commands.Bot(command_prefix='$', intents=intents)

@client.event # sync your slash commands and show when the bot is ready
async def on_ready():
    try:
        synced = await client.tree.sync()
        print(F'Synced {len(synced)} tree command(s).')
        print(F'{client.user} is running.')
    except Exception as e:
        print(F'Could Not Sync Tree: {e}')
      
