# import discord.py
import discord
from discord.ext import commands
from discord import app_commands

# import os and load_dotenv to load the .env file 
from os import getenv
from dotenv import load_dotenv

#import commands from bot_methods.py
import bot_methods


# load discord bot token from .env file
load_dotenv()
TOKEN = getenv("DISCORD_TOKEN")

# Set all non privlleged gateway intents for discord bot
# https://discordpy.readthedocs.io/en/latest/api.html#discord.Intents
intents = discord.Intents.all() # use discord.Intents.default() if you don't need them all

# Create a new discord client with the intents to connect it to the discord gateway
# You can name it bot or application it is up to you
client = discord.Client(intents=intents)

# Set bot prefix
client = commands.Bot(command_prefix='$', intents=intents)

# Listener for when the bot has been connected to the gateway and synced slash commands
@client.event
async def on_ready():
    try:
        synced = await client.tree.sync()
        print(F'Synced {len(synced)} tree command(s).')
        print(F'{client.user} is ready.')
    except Exception as e:
        print(F'Could Not Sync Tree: {e}')

@client.command(name='run')
async def run_code(ctx, *, code: str):
    await bot_methods.run(ctx, code=code)


client.run(token=TOKEN)



