from dotenv import load_dotenv
import os
import discord
from discord import Intents
from discord.ext import commands
from libs.Database import Database

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
MONGODB_TOKEN = os.getenv('MONGODB_TOKEN')

db = Database(MONGODB_TOKEN)
intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    print(f'Living at {len(bot.guilds)} guild(s)...')


@bot.command()
async def ping(ctx):
    print("pong")
    if ctx.author == bot.user:
        return
    await ctx.reply(f'Pong! In {round(bot.latency * 1000)}ms')

bot.run(TOKEN)
