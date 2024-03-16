# Discord_Bot_Workshop
A repo on how to setup a discord bot step by step!
**You need**
- Discord account
- Python installed
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
Head over to the [discord developer page](https://discord.com/developers/applications), log in, and in the top right click `New Application` and type the name of your Discord bot.

> [!NOTE]
> For simplicity we will not select a team, but you can create a team in the 'Teams' tab and add people that will be associated with the development of the bot!

Click on the `Bot` tab and then go to `Privileged Gateway Intents`. These are the different types of data that your bot will have access to when in a server. You can read about them by clicking the [links](https://discord.com/developers/docs/topics/gateway#gateway-intents) to see what each intent covers and if you may need a single or multiple when you make your own bot!

> [!NOTE]
> For simplicity, we will select all gateway intents in case you want to add more to your first bot. In real practice, you want to read up on these intents and see which you really do need since when you apply to get your bot verified at 75 servers, discord will ask you why you are using them! You will need to apply for gateway intents separately with the verification process. If you have any questions about verifying a discord bot, ask me ([@JOwen-ster](https://github.com/JOwen-ster) on GitHub or [`typos.`](https://discord.com/) on Discord) since I have a bot that is in 200+ servers and is verified!

Next, head over to the `OAuth2` Tab and then in the dropdown menu for `Default Authorization Link`, click on `In-app Authorization`.
* Under Scopes -> click `bot`
* Under Bot Permissions -> click any permissions that your bot will need.

This will make it so people can add your bot from its profile with these selected perms to any server they have the `Manage Server` permission in.

> [!NOTE]
> For this workshop we will use the `Administrator` perm since it will cause no conflict since the bot will have access to all channels with all permissions.
> Bots are treated like regular members/users with their access to channels and ways they interact with the server like being able to manage messages is not a usual default perm for most servers, it is not for a bot unless you give it that perm.

> [!WARNING]
> Unless your Discord bot's function is for server management such as raid protection, server setup, moderation, or various non member interactive things, I would **NOT** set your permissions as Admin just because it is "easy". From my bot developing experience, when getting bots into bigger servers, some owners really wanna limit what it can do for security purposes. As an example, if your token gets exposed, someone logs into your bot and with a total of 20 lines of code (not joking) every server that bot is in, it will nuke, mass ping, and ban every member.

Finally, scroll down till you see `OAuth2 URL Generator`
* Under Scopes -> click `bot`
* Under Bot Permissions -> click any permissions that your bot will need.

This will create a link that people can click to add your bot to any server with these selected perms to any server they have the `Manage Server` permission in.

### Before we get coding...
> [!IMPORTANT]
> Go to the `Bot` tab.
> Click `Reset Token` near the top of the page

***__COPY AND SAVE THIS TOKEN SOMEWHERE SECURE AND SOMEWHERE YOU CAN ACCESS IT__***

> [!CAUTION]
> **THIS TOKEN IS HOW TO CONNECT TO YOUR APPLICATION WITH CODE, NO ONE NEEDS ANYTHING ELSE TO CONNECT/LOG INTO YOUR BOT EXCEPT THE MOST RECENT TOKEN. NEVER POST IT OR YOU RISK YOUR BOT GETTING HIGHJACKED**

> [!CAUTION]
> If you do not gitignore the `.env` file in your `.gitignore` (which is where you put your token, not in your bot code) (and you should use a .env for storing your token in code and a .gitignore to hide private files), then GitHub bots **will** scrape your token (it has happened to me) and may use it. Discord will hopefully send you a message very fast saying they caught it and reset it since they are also scraping for Discord Bot Tokens to watch out for you and keeping your bots secure :)

![image](https://github.com/JOwen-ster/Discord_Bot_Workshop_2024/assets/111905194/79737d0c-b11f-4ee2-a0e2-f23a2d7f92f7)

## Coding the Actual Discord Bot
By the end, we will have a bot that is able to run code that you paste into discord using pistonapi!
We will be using the [discord.py](https://discordpy.readthedocs.io/en/stable/) api wrapper in this workshop.

[Read the docs (How to do Commands)](https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html)

[Read the docs (How to do Events/Listeners)](https://discordpy.readthedocs.io/en/stable/api.html?highlight=event#discord-api-events)

Go ahead and `pip install` the required libraries for Discord and Environment Variables.

For Windows you can execute [discord_dependencies.bat](/discord_dependencies.bat) found in this repo or run the following command...

```
pip install discord && pip install python-dotenv && pip install pistonapi
```
After you have successfully installed the Python Discord and dotenv libraries, create a new folder OUTSIDE THIS DIRECTORY (Since this is going to be your bot) and name it something like `mydiscordbot` and open it up with your favorite code editor.

### IN THE FOLDER
Create a new file named `.env` (no name before the dot) and put the following in it.
```
DISCORD_TOKEN = 'YOUR_BOT_TOKEN_GOES_HERE'
```

Create a new file named `.gitignore` (no name before the dot) and put the following inside it.
```
.env
```

Create a new file and name it `bot.py`
- Use my [discord python bot template](/bot_template.py) to get all the runner code and put it into your `bot.py` file (found in this repository).



