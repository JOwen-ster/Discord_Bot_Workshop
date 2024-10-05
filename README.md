# Discord_Bot_Workshop
A repo on how to setup a discord bot step by step!
**You will need...**
- A [Discord](https://discord.com/) account
- [Python](https://www.python.org/) installed
  - If you want to use JavaScript to make a discord bot, I recommend using this [template](https://github.com/PillowGit/base-discord-js-bot) made by [@PillowGit](https://github.com/PillowGit) for the coding portion
- Internet access
- A IDE to edit and run code (Like Visual Studio Code)


***CLONE THIS REPOSITORY***
- [x] HTTPS
```
git clone https://github.com/JOwen-ster/Discord_Bot_Workshop.git
```

- [X] SSH
```
git clone git@github.com:JOwen-ster/Discord_Bot_Workshop.git
```

- [X] GitHub CLI
```
gh repo clone JOwen-ster/Discord_Bot_Workshop
```

![Discord_Python_Logo](https://images.opencollective.com/discordpy/25fb26d/logo/256.png)

## Creating Your Application
Head over to the [discord developer page](https://discord.com/developers/applications), log in, and at the top right of your screen click `New Application`, type the name of your Discord bot, and then click `create`

> [!NOTE]
> For simplicity we will not select a team, but you can create a team in the 'Teams' tab and add people that will be associated with the development of the bot!

On the side, click on the `Bot` tab and then scroll down to `Privileged Gateway Intents` on that page. These are the different types of data that your bot will have access to when in a server. You can read about them on [developer gateway intents page](https://discord.com/developers/docs/topics/gateway#gateway-intents) to see what each intent covers and if you may need a single or multiple when you make your own bot!

> [!NOTE]
> For simplicity, we will toggle on all gateway intents in case you want to add more to your first bot. In real practice, you want to read up on these intents and see which your bot would need since when you apply to get your bot verified at 75 servers, Discord will ask you why you are using them! You will need to apply for gateway intents separately with the verification process. If you have any questions about verifying a discord bot, ask me on Discord (`typos.`) since I have a bot that is in 300+ servers and is verified!

Next, on the side of your screen click on the `Installation` tab.

* Scroll down to the `Install Link` dropdown menu, make sure `Discord Provided Link` is selected.

Now, scroll down to `Default Install Settings` and click on the `SCOPES` dropdown menu under `Guild Install`.
* Under the `SCOPES` -> select `bot`.
* Under `PERMISSIONS` -> select any server permissions that your bot will need to fully function.

> [!NOTE]
> For this workshop we will use the `Administrator` permission for ease. Giving a user or bot `Administrator` will give access to all channels with all permissions regardless of how they are setup in your server.
> Bots are treated like regular membersm in a server with their access to channels and ways they interact with the server. For example able to `manage member` is not a usual default permission for most servers, it will not be for a bot unless you give it that permission.

> [!WARNING]
> Unless your Discord bot's function is for server management such as raid protection, server setup, moderation, or various non member interactive things, I would **NOT** set your permission to `Administrator` just because it is "easy". From my bot developing experience, when getting bots into bigger servers, some owners really wanna limit what it can do for security purposes. As an example, if your token gets exposed, someone logs into your bot and with a total of 20 lines of code (not joking) every server that bot is in, it will nuke, mass ping, and ban every member.

Under `Install Link`, there is a link you send to others. When clicked, that user can add your bot with all the permissions you selected to any server they have the `Manage Server` permission in (or it will not appear under the list of servers when adding).


### Before we get coding...
> [!IMPORTANT]
> Go to the `Bot` tab.
> Click `Reset Token` near the top of the page

# ***__COPY AND SAVE THIS TOKEN SOMEWHERE SECURE AND SOMEWHERE YOU CAN ACCESS IT__***

> [!CAUTION]
> # **THIS TOKEN IS HOW TO CONNECT TO YOUR APPLICATION WITH CODE, NO ONE NEEDS ANYTHING ELSE TO CONNECT/LOG INTO YOUR BOT EXCEPT THE MOST RECENT TOKEN. NEVER POST IT OR YOU RISK YOUR BOT GETTING HIGHJACKED**

> [!CAUTION]
> If you do not gitignore the `.env` file in your `.gitignore` file (the `.env` file is where you should put your token, not in your bot code) , then GitHub bots **will** scrape your token (it has happened to me) and may use it. Discord will hopefully send you a message very fast saying they caught it and reset it since they are also scraping for Discord Bot Tokens to watch out for you and keeping your bots secure :)

![image](https://github.com/JOwen-ster/Discord_Bot_Workshop_2024/assets/111905194/79737d0c-b11f-4ee2-a0e2-f23a2d7f92f7)

## Coding the Actual Discord Bot
By the end, we will have a bot that is able to run Python code that you paste into Discord using pistonapi!
We will be using the [discord.py](https://discordpy.readthedocs.io/en/stable/) API wrapper in this workshop.

[Read the docs (How to do Commands)](https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html)

[Read the docs (How to do Events/Listeners)](https://discordpy.readthedocs.io/en/stable/api.html?highlight=event#discord-api-events)

Go ahead and install the required libraries listen bellow for Discord, Environment Variables, and PistonAPI (used to run code safely and send the output which is what our bot will do).

Install from the requirements.txt in this repo...
```
pip install -r requirements.txt
```
- or
Pip install manually with the following command...
```
pip install discord && pip install python-dotenv && pip install pistonapi
```
- or
for Windows you can double click and execute [dependencies.bat](/dependencies.bat) in file explorer found in this repositorys directory.

After you have successfully installed the libraries...

## **Open your favorite code IDE!**

Create a new file named `.env` (no name before the dot) and put the following in it.
```
DISCORD_TOKEN = 'YOUR_BOT_TOKEN_GOES_HERE'
```

Normally you would create a new file named `.gitignore` (no name before the dot) and put the following inside it.
```
.env
```

But I have already included it. Just know that if you choose to upload your bot code to GitHub, anything in `.gitignore` will not be included.

Create a new file and name it `bot.py`
- Use my [discord python bot template](/TEMPLATE.py) to paste the runner code in into `bot.py`.
- Add your commands  by reading the documentation, looking things up, and asking questions (refer to the [methods file](/BOT_METHODS.py) for some starter commands and explanation) 
- Run your code when done

If you see the following (Along with YOU_BOT_USERNAME is ready) in your terminal output, your bot should be up and running!

![image](https://github.com/JOwen-ster/Discord_Bot_Workshop/assets/111905194/8ba8730a-1464-4111-ac54-46a574f03a1f)

Go ahead and use the `OAuth2 URL Generator` link we made and add your bot to a testing server and run the command!

![image](https://github.com/JOwen-ster/Discord_Bot_Workshop/assets/111905194/25b69528-0056-410f-baae-df36155837c1)




# FINAL BOT CODE ANSWER - no peaking :)
<details>
  <summary>Bot.py Answer</summary>
  
```py  
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
# https://discordpy.readthedocs.io/en/latest/api.html#discord.Intents
# For today we need the message_content intent so using .all() covers this.
intents = discord.Intents.all() # use discord.Intents.default() if you don't need them all.
# If we were to not use .all()...
# intents = discord.Intents.default()
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
@client.tree.command(name="ping", description="Check the bot's latency")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong! I responded in {round(client.latency * 1000)}ms')

# Our first command will go here!
# First we need to tell Discord that this will be a new command
# We specify a name for our command.
# If we don't specify a name, the function name will be used as the command name
@client.command(name='run')
# We use the async keyword to define an asynchronous function
# Async means that the function will run in the background
#and not block the rest of the code from running so the bot can continue to respond to other events
async def run_code(ctx, *, code: str):
    # We passed in the context object which is the trigger for the command (this is required always)
    # We pass a string called code which will be the code we want to run
    # We are using the * symbol so we can pass in multiple arguments or multiple words/lines of code
    # REFER TO BOT_METHODS.PY FOR MORE EXPLANATION
    
    # We call the run method from bot_methods.py and pass in its parameters
    # We use await to tell the bot to wait for the method to finish before continuing
    await bot_methods.run(ctx, code=code)

client.run(TOKEN)
```
  
</details>
