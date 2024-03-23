import discord
from discord.ext import commands
from ..libs.chess_crawler import *

class Chess_crawler(commands.Cogs):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def profile(self, ctx, user = None):
        username = user or ctx.author
        profile = get_player(username)
        await ctx.send(str(profile))
