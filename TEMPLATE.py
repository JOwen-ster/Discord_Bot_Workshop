# Import discord.py
import discord
from discord.ext import commands
from discord import app_commands

# Import os and load_dotenv to load your bot token from the .env file 
from os import getenv
from dotenv import load_dotenv

# Import commands from bot_methods.py
import BOT_METHODS


# Load discord bot token from .env file
load_dotenv()
TOKEN = getenv("DISCORD_TOKEN")

# Set all non privlleged gateway intents for discord bot
intents = discord.Intents.all() # use discord.Intents.default() if you don't need them all
# for example, if you only need the guilds and message_content intents
# https://discordpy.readthedocs.io/en/latest/api.html#discord.Intents
# intents = discord.Intents.default()
# intents.guilds = True
# intents.message_content = True

# Set a bot prefix to listen for commands
# Create a new discord client with the intents to connect it to the discord gateway
# You can name it bot, application, client (anything to refer to your bot) it is up to you
BOT_PREFIX = '$'
client = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

# Listener for when the bot has been connected to the gateway and synced slash commands
@client.event
async def on_ready():
    try:
        synced = await client.tree.sync()
        print(F'Synced {len(synced)} tree command(s).')
        print(F'{client.user} is ready.')
    except Exception as e:
        print(F'Could Not Sync Tree: {e}')

# How to make a slash command


# Our first command will go here!
# First we need to tell Discord that this will be a new command
# We specify a name for our command.
# If we don't specify a name, the function name will be used as the command name
##### CODE HERE #####

# We use the async keyword to define an asynchronous function
# Async means that the function will run in the background
#and not block the rest of the code from running so the bot can continue to respond to other events
##### CODE HERE #####

    # We passed in the context object which is the trigger for the command (this is required always)
    # We pass a string called code which will be the code we want to run
    # We are using the * symbol so we can pass in multiple arguments or multiple words/lines of code
    # REFER TO BOT_METHODS.PY FOR MORE EXPLANATION
    
    # We call the run method from bot_methods.py and pass in its parameters
    # We use await to tell the bot to wait for the method to finish before continuing
    ##### CODE HERE #####
    
client.run(token=TOKEN)

