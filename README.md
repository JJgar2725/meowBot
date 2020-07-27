# meowBot >.< - a simple discord bot

Hello! Welcome to ***meowBot***! :3

This project mainly originated from me seeking a new programming experience other than C++ - Python. 
With this, I could step into the fundamentals of Python and learn a new library / framework used to create Discord bots.
This simple framework is known as ***discord.py***, and with it comes many functions that Discord users use on a daily basis!
Hence, my inspiration to create my own discord bot came with consistently using Discord as a platform to communicate
with friends and family. 

Below can be seen a general outline of the things that meowBot can accomplish!

## **Installation**

To install and actually run meowBot on your local machine, perform the following steps.
1. Clone the repo to your local machine - store it in a Projects folder preferably.
2. Create a virtual environment by running ```python3 -m venv meowBot-env``` in the directory of the project. 
You can activate the virtual environment by running ```meowBot-env\Scripts\activate.bat``` on Windows, and ```source meowBot-env/bin/activate``` on Mac or Linux. From here, run ```pip install -U discord.py```.
3. Install the dependencies from the requirements.txt file by running ```pip install -U -r requirements.txt```. 
4. From here, create a ```.env``` file that contains the following fields. 
```
BOT_TOKEN = "your_bot_token"
CLIENT_ID =  "your_client_ID"
LOGS_ID = "your_logs_channel_id"
GENERAL_ID = "your_general_channel_id"
```

## ***General Commands***
Some useful commands to access meowBot:

```m.help``` - Lists the commands currently available for the user.

```m.musichelp``` - Lists the commands to access music functions.

```m.misc``` - Lists fun and miscellaneous functions.

```m.intro``` - Greets the user.

```m.users``` - Prints number of users.

```m.purge (num)``` - Purges however many messages you provide it prior to sending command.

## ***Music Commands***
Some useful commands to access meowBot's music functionality:

```m.join``` - Adds the bot to a voice channel if user is already in one. Otherwise, nothing will happen.

```m.leave``` - Takes meowBot out of whatever channel the user is in.

```m.play (url) | m.play search term``` - Plays a song from youtube given by the user.

```m.pause``` - Pauses the current song playing.

```m.resume``` - Resumes the current song on queue.

```m.stop``` - Completely stops any audio from playing on meowBot.

## ***Miscellaneous Commands***
Some fun and miscellaneous functions that meowBot offers:

```m.quote``` - Prints a random quote for you fellas feeling under the weather.

```m.dadprogjoke``` - Provides the user with a funny dad programming joke, if you're into that stuff.

```m.jojo``` - Plays the infamous Giorno's Theme from Jojo's Bizarre Adventure. Pretty cool, I know.

## ***Developer Commands***
Listed below are some commands created in order to ease workflow as I developed meowBot:

```m.load (cog file name)``` - Loads a specified cog back into the bot after edits are finished.

```m.reload (cog file name)``` - Reloads a specified cog into the bot during runtime.

```m.unload (cog file name)``` - Unloads a specified cog off the bot in order to allow for edits.

## **Behind The Scenes**
Things that meowBot could possibly perform in the background include:

```on_message_delete``` - Sends a warning message in a logs channel notifying moderators who deleted a message.

```on_member_join``` - Greets the user upon joining the server, and assigns the member with an introductory role.