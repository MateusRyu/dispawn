import discord
from discord.ext import commands
from libs.chess_crawler import *
from datetime import datetime

class ChessCrawler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.timeformat = "%d/%m/%Y, %H:%M"

    # TODO: criar fila de request para adequar à 1 única requisição por vez
    async def run_request(request, args):
        pass
    
    def convert_boolean(self, boolean):
        if boolean:
            return "sim"
        else:
            return "não"
    
    @commands.command()
    async def profile(self, ctx, user = None):
        print("Start to get profile..")
        username = user or ctx.author
        profile = get_player(username)
        now = datetime.now()
        timestamp = now.strftime(self.timeformat)

        last_online = datetime.fromtimestamp(profile["last_online"])
        joined = datetime.fromtimestamp(profile["joined"])
        country = profile["country"]
        name = profile["username"]
        if "name" in profile:
            name = profile["name"]

        embed = discord.Embed(title=name, description="Perfil do chess.com")
        embed.set_author(name=f"@{profile['username']}", url=profile["url"])
        if "avatar" in profile:
            embed.set_thumbnail(url=profile["avatar"])

        embed.add_field(name="ID", value=profile["player_id"])
        embed.add_field(name="Seguidores", value=profile["followers"])
        embed.add_field(name="País", value=f"{country['name']} ({country['code']})")
        embed.add_field(name="Última vez online", value=last_online.strftime(self.timeformat))
        embed.add_field(name="Conta criada em", value=joined.strftime(self.timeformat))
        embed.add_field(name="Conta", value=profile["status"])
        embed.add_field(name="Streamer", value=self.convert_boolean(profile["is_streamer"]))
        if "twitch_url" in profile:
            embed.add_field(name="Twitch", value=profile["twitch_url"])
        embed.add_field(name="Verificado", value=self.convert_boolean(profile["verified"]))
        embed.add_field(name="Liga", value=profile["league"])

        if "title" in profile:
            embed.add_field(name="Titulo", value=profile["title"])
            embed.add_field(name="Rating FIDE", value=profile["fide"])


        embed.set_footer(text=f"Dados coletados em: {timestamp}")
        embed.color = discord.Color.green()

        await ctx.send(str(profile))
        await ctx.send(embed=embed)
        print("Profile was returned to the author!")

async def setup(bot):
    await bot.add_cog(ChessCrawler(bot))
