# Import discord.py
import discord
from discord.ext import commands
from discord import app_commands

# Import os and load_dotenv to load your bot token from the .env file 
from os import getenv
from dotenv import load_dotenv

# Import piston API to run code
from pistonapi import PistonAPI


# Set all non privlleged gateway intents for discord bot
# https://discordpy.readthedocs.io/en/latest/api.html#discord.Intents
intents = discord.Intents.default() # Can also use discord.Intents.all() if you need them all

# Set a bot prefix to listen for commands
# Create a new discord client with the intents to connect it to the discord gateway
# You can name it bot, application, client (anything to refer to your bot) it is up to you
BOT_PREFIX = '$'
client = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

# Keep in mind we do not need to use the @client decorator
#if we are just defining a function that will be called in different file
#which in this case is template.py where our bot will be ran from.

# We only need to use the @client decorator if
#we want to associate it with an action/command/event. The decorator will not transfer.

# Decorators can be...
# 1. A function name associated with an action.
#@client.event # decorator like a sync slash commands and show when the bot is ready
async def on_ready(): # listener for when the bot has been connected to the gateway (good practice)
    try:
        synced = await client.tree.sync()
        print(F'Synced {len(synced)} tree command(s).')
        print(F'{client.user} is ready.')
    except Exception as e:
        print(F'Could Not Sync Tree: {e}')

# 2. Using the @client.listen decorator, you can just pass in the event name as a string without overloading the function name.
#@client.listen('on_message') # listener for events
async def mylistener(message):
    if message.author == client.user:
        return
    if message.content == 'hello':
        await message.channel.send('hi')
# When overloading the function name, you can use the same function name for multiple event handelers
# This also applies the client.listen() decorator.
# When using the overloaded method, you put await client.process_commands(message) at the end of the function to allow the bot to process commands. 

# slash command (tree command)
#@client.tree.command(name="ping", description="Check the bot's latency")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong! I responded in {round(client.latency * 1000)}ms')

# slash command with an invisible response (ephemeral)
#@client.tree.command(name="secretnumber", description="Get a random number within your given range")
async def secretnumber(interaction: discord.Interaction, min: int, max: int):
    await interaction.response.send_message(f'Your secret random number is {randint(min, max)}', ephemeral=True) # ephemeral means only the user can see the response

# slash command with an optional parameter by setting the default to None
#@client.tree.command(name="copyme", description="Send a message back to you with the same content")
async def copyme(interaction: discord.Interaction, phrase: str, optional_phrase: str=None):
    if optional_phrase is None:
        await interaction.response.send_message(f'You said "{phrase}"', ephemeral=True)
    else:
        await interaction.response.send_message(f'You said "{phrase}" and your optional phrase was "{optional_phrase}"', ephemeral=True)

#@client.command(name='dms') # regular prefix command, not a slash command
async def cmd_dms(ctx): # name is specified, so $dms would work but not $cmd_dms
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

# If you want to pass an unknown amount of parameters with a slash command,
# I would recommend splitting the one paramater by spaces into a list of strings then iterate the list.
# EX. parameter_list: list[str] = myparameter.split()
#@client.command() # name is not specified, so we use the function name for the command name
async def repeat(ctx, *, arg): # passing unknown amount of parameters without parsing them
    await ctx.send(arg) # arg is a string

#@client.command()
async def repeatparams(ctx, *args): # passing and parsing unknown amount of parameters
    arguments = ', '.join(args) # *args is a tuple
    await ctx.send(f'{len(args)} arguments: {arguments}')

#@client.command()
async def run(ctx, *, code: str): # run code that is sent in code block format
    piston = PistonAPI()
    await ctx.channel.send('Running...')
    
    if code.startswith('```py') and code.endswith('```'):
        code = code[5:-3]
        fcode = f'''{code}'''
        response = piston.execute(language="py3", version="3.10.0", code=fcode)
        await ctx.channel.send(f'''```\n{response}```''', reference=ctx.message)
    else:
        howto = '`$run\n```py\nCODE_HERE\n``` `'
        await ctx.channel.send(f'Please use code blocks to run code.\n{howto}', reference=ctx.message)
