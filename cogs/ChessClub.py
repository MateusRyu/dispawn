import discord
from discord.ext import commands

class ChessClub(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.club_link = ""
        self.tournament_links = {}
        super().__init__()

    @commands.command(name='setClubLink')
    @commands.has_permissions(manage_guild=True)
    async def set_club_link(self, ctx, *, link:str):
        self.club_link = link
        await interact.response.send_message(f'Definindo o link do clube para: {link}')

    
async def setup(bot):
    await bot.add_cog(ChessClub(bot))
