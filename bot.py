# import discord api
import discord
from discord.ext import commands
from discord import app_commands

# import os and load_dotenv to load the .env file 
import os
from dotenv import load_dotenv


# load discord bot token from .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Set all non privlleged gateway intents for discord bot
intents = discord.Intents.all() # use discord.Intents.default() if you don't need all
# https://discordpy.readthedocs.io/en/latest/api.html#discord.Intents
client = discord.Client(intents=intents) # create a new discord client with the intents to connect it to the discord gateway

# Set bot prefix
client = commands.Bot(command_prefix='$', intents=intents)

# Decorators can be...
# 1. A function name associated with an action.
@client.event # decorator like a sync slash commands and show when the bot is ready
async def on_ready(): # listener for when the bot has been connected to the gateway
    try:
        synced = await client.tree.sync()
        print(F'Synced {len(synced)} tree command(s).')
        print(F'{client.user} is ready.')
    except Exception as e:
        print(F'Could Not Sync Tree: {e}')
        
# 2. Using the @client.listen decorator, you can just pass in the event name as a string without overloading the function name.
@client.listen('on_message') # listener for events
async def mylistener(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send('hi')
# When overloading the function name, you can use the same function name for multiple event handelers
# This also applies the client.listen() decorator.
# When using the overloaded method, you put await client.process_commands(message) at the end of the function to allow the bot to process commands. 

@client.tree.command(name="ping", description="Check the bot's latency") # slash command
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong! I responded in{round(client.latency * 1000)}ms')
    
@client.command() # regular prefix command, not a slash command
async def dms(ctx):
    # if you want to test dms without sending a message do this...
    # try:
    #     await user.send()
    # except discord.Forbidden:
    #     await ctx.channel.send("You do not have direct messages from server members enabled! Enable them in your Discord 'Privacy & Safety' settings.")
    # except discord.HTTPException:
    #     await ctx.channel.send("You have direct messages from server members enabled!")
    try:
        await ctx.author.send('You have dms enabled from server members!')
    except discord.Forbidden:
        await ctx.channel.send("Please enable 'Allow direct messages from server members' in your Discord 'Privacy & Safety' settings.", ephemeral=True)
        
@client.command()
async def repeatparams(ctx, *args): # passing and parsing parameters from a command
    arguments = ', '.join(args) # *args is a tuple
    await ctx.send(f'{len(args)} arguments: {arguments}')        
        
@client.command()
async def repeat(ctx, *, arg): # passing many parameters without parsing them
    await ctx.send(arg) # arg is a string
    
client.run(TOKEN)

