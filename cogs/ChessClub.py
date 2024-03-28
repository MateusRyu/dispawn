from discord.ext import commands
from discord import app_commands, Interaction, ButtonStyle
from discord.ui import View, Button
from libs.database import insert_club, get_club, update_club, delete_club

class ChessClub(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()


    @app_commands.command()
    @app_commands.describe(link="Link para o clube", nome="Nome do clube")
    @commands.has_permissions(manage_guild=True)
    async def new_club(self, interact: Interaction, *, link:str, nome:str):
        await interact.response.send_message(f'Criando clube com o nome `{nome}` e link `{link}`...', ephemeral=True)
        result = insert_club(interact.guild_id, link, nome)
        print(str(result))
        await interact.followup.send('Clube criado com sucesso!', ephemeral=True)


    @app_commands.command()
    @app_commands.describe(link="Link para o clube", nome="Nome do clube")
    @commands.has_permissions(manage_guild=True)
    async def update_club(self, interact: Interaction, *, link:str = None, nome:str = None):
        new_values = {}
        await interact.response.send_message('Atualizando dados do clube...', ephemeral=True)
        if link:
            new_values["club_link"] = link
            await interact.followup.send(f'Definindo o link do clube para `{link}`...', ephemeral=True)

        if nome:
            new_values["club_name"] = nome
            await interact.followup.send(f'Definindo o nome do clube para `{nome}`...', ephemeral=True)

        result = update_club(interact.guild_id, new_values)
        print(str(result))
        await interact.followup.send('Atualização completa!', ephemeral=True)

    @app_commands.command()
    async def club(self, interact: Interaction):
        club = get_club(interact.guild_id)
        if club:
            await interact.response.send_message(f'O link para o clube `{club["club_name"]}` é: {club["club_link"]}')
        else:
            await interact.response.send_message("Este servidor não tem nenhum clube.")

    @app_commands.command()
    @commands.has_permissions(manage_guild=True)
    async def delete_club(self, interact: Interaction):
        async def confirm(interact: Interaction):
            response = delete_club(interact.guild_id)
            print(str(response))
            await interact.response.send_message('Clube excluido com sucesso!', ephemeral=True)

        async def cancel(interact: Interaction):
            await interact.response.send_message('Ação cancelada!', ephemeral=True)

        view = View()
        yes = Button(label="Sim", style=ButtonStyle.green)
        no = Button(label="Não", style=ButtonStyle.red)

        yes.callback = confirm
        no.callback = cancel

        view.add_item(yes)
        view.add_item(no)
        await interact.response.send_message(f'Tem certeza que quer excluir o clube?', ephemeral=True)
        await interact.followup.send(view=view)
    
async def setup(bot):
    await bot.add_cog(ChessClub(bot))
