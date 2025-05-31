import logging
import os
from logging.handlers import RotatingFileHandler

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
AI_APP_USER_IDS = [int(bot_id.strip()) for bot_id in os.getenv('AI_APP_USER_IDS').split(',')]

# Create a rotating file handler for the bot to log to.
# It'll write to `discord.log` in the local folder, and whenever that file gets to 5 megabytes,
# it'll move the contents to `discord.log.#`, then continue appending to `discord.log`.
log_handler = RotatingFileHandler(
    'discord.log',
    mode='a',
    # Rotate files every 5 MB.
    maxBytes=5*1024*1024,
    # Keep 10 backup files, for a total of up to 55MB of logs.
    backupCount=10,
    encoding='utf-8'
)

# Define the bot using the intents it needs for message handling.
intents = discord.Intents.default()
intents.message_content = True
intents.guild_messages = True
bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)

@bot.event
async def on_ready():
    """
    Prints a message to the console when the bot comes online, so we know it's running.
    """
    print(f"{bot.user.name} bot is online!")


@bot.event
async def on_message(message):
    """
    Looks for messages from the AI image apps that Discord offers and deletes them, then
    informs the channel that those functions are disabled on this server.
    """
    if message.author == bot.user:
        # Don't interact at all with the bot's own messages.
        return

    # If the message was authored by a known Discord AI app ID, delete it and say why.
    if message.author.id in AI_APP_USER_IDS:
        await message.delete()
        await message.channel.send(
            f"Discord's {message.author.mention} AI image manipulation app is disabled on this server."
        )
        # Also print to the console what we did, so something other than the on_ready() message shows
        # up there.
        print(
            f"Blocked a message from {message.author} in #{message.channel} on the '{message.channel.guild}' server."
        )

    # The tutorial I watched said this has to be here, but it didn't say why.
    await bot.process_commands(message)


# Users on the server can get the bot to acknowledge that it's running by saying:
# !Anti-AI
@bot.group(name="Anti-AI")
async def base(ctx):
    if ctx.invoked_subcommand is None:
        # Only say this is the user did not invoke the poke subcommand.
        await ctx.reply("Anti-AI bot is online!")
        print(f"Asserted presence to {ctx.author} in #{ctx.channel} on the '{ctx.guild}' server.")


@base.command(name="poke")
async def poke(ctx):
    """
    Pokes the user when they type "!Anti-AI poke".
    """
    await ctx.reply("*pokes back*")
    print(f"Poked by {ctx.author} in #{ctx.channel} on the '{ctx.guild}' server.")


bot.run(token, log_handler=log_handler, log_level=logging.INFO)
