import discord
from discord.ext import commands
import os
from os import getenv
from dotenv import load_dotenv
import datetime as dt
from config import PREFIX

load_dotenv()

# Initialise bot


# Create custom bot so we can run custom code when the bot is stopped
class Bot(commands.Bot):
    start_time = dt.datetime.utcnow()


intents = discord.Intents.all()
bot = Bot(command_prefix=commands.when_mentioned_or(PREFIX), case_insensitive=True, owner_ids=[114352655857483782],
          allowed_mentions=discord.AllowedMentions(roles=False, everyone=False), intents=intents,
          chunk_guilds_at_startup=False)

bot.remove_command("help")


@bot.event
async def on_ready():
    # Print startup message
    startup = bot.user.name + " is running"
    print(startup)
    print("-" * len(startup))  # Print a line of dashes as long as the last print line for neatness
    # Load cogs
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            print("Loading: cogs." + filename[:-3])
            await bot.load_extension("cogs." + filename[:-3])


# Start the bot
bot.run(getenv("BOT_TOKEN"))
