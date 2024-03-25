from dotenv import load_dotenv
import os
import discord
from discord import Intents, Interaction, app_commands
from discord.ext import commands
from libs.Database import Database

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
MONGODB_TOKEN = os.getenv('MONGODB_TOKEN')

db = Database(MONGODB_TOKEN)
intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)

async def load_cogs(path):
    print("Stating to load cogs...")
    cogs_amount = 0
    for file in os.listdir(path):
        if file.endswith(".py"):
            await bot.load_extension(f"{path}.{file[:-3]}")
            cogs_amount += 1
    print(f"Loaded {cogs_amount} cogs!")

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    print(f'Living at {len(bot.guilds)} guild(s)...')
    await load_cogs("cogs")


@bot.command()
async def ping(ctx):
    print("pong")
    if not ctx.author.bot:
        await ctx.reply(f'Pong! In {round(bot.latency * 1000)}ms')

@bot.hybrid_command()
@commands.is_owner()
async def sync(ctx):
    print("Syncs...")
    commands_list = await bot.tree.sync()
    print("Sync has been completed")
    await ctx.reply(f"{len(commands_list)} commands got synced!")

bot.run(TOKEN)
