from dotenv import load_dotenv
import os
import discord
from libs.Database import Database

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
MONGODB_TOKEN = os.getenv('MONGODB_TOKEN')

db = Database(MONGODB_TOKEN)
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(f'Living at {len(client.guilds)} guild(s)...')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(';hello'):
        await message.channel.send('Hello!')

    elif message.content.startswith(';db_ping'):
        feedback = 'Banco de dados conectado' if db.ping() else 'Banco de dados não conectado'
        await message.channel.send(feedback)

client.run(TOKEN)
