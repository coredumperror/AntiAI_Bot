# Anti-AI Discord Bot

Anti-AI is a Discord bot that automatically deletes any messages sent to any channel in your server by the following
Discord AI image manipulation apps:

* @Viggle
* @Glifbot
* @InsightFaceSwap

This prevents users who attempt to use them from receiving the results of the AI app's manipulations.
It also _seems_ to prevent the bot from actually performing the image manipulation task in the first place, since
it never sends its followup message with the results.

### To invite the bot to your server, visit this URL:
https://discord.com/oauth2/authorize?client_id=1374973550921908244&permissions=292057852928&integration_type=0&scope=bot

Once it's installed on your server, you can confirm that it's running by typing `!Anti-AI`. If it successfully replies
to your message, it will be primed to automatically delete messages from the Discord AI apps.


## How to run this bot yourself

If you'd like to run your own instance of Anti-AI, you just need to install the requirements into a modern Python
interpreter, get yourself a Bot Token from Discord, copy `.env.example` to `.env`, and put the token into that file.
Then run `python main.py`.

[This tutorial](https://www.youtube.com/watch?v=YD_N6Ffoojw) was instrumental in helping me figure out how to make
Anti-AI, so you might find it helpful, too.
