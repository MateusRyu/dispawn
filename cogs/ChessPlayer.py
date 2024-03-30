from discord.ext import commands
from discord import app_commands, Interaction, ButtonStyle, Member
from discord.ui import View, Button
from libs.database import insert_player, get_player, update_player, delete_player

class ChessPlayer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()


    @app_commands.command()
    @app_commands.describe(username = "nick único que cada jogador escolhe ao criar a conta", invite_link = "link para poder te convidar como amigo no site (opcional)")
    async def new_player(self, interact: Interaction, *, username:str, invite_link:str=""):
        site = "chessDotCom"
        feedback = f'Cadastrando {interact.user.display_name} com nick `{username}`'
        if invite_link != "":
            feedback = feedback + f' e link para convite de amizade `{invite_link}`'

        async def confirm(interact: Interaction):
            response = insert_player(interact.guild_id, interact.user.id, site, username, invite_link)
            await interact.response.send_message('Cadastro concluido com sucesso!', ephemeral=True)

        async def cancel(interact: Interaction):
            await interact.response.send_message('Ação cancelada!', ephemeral=True)

        view = View()
        yes = Button(label="Sim", style=ButtonStyle.green)
        no = Button(label="Não", style=ButtonStyle.red)

        yes.callback = confirm
        no.callback = cancel

        view.add_item(yes)
        view.add_item(no)

        await interact.response.send_message(feedback, ephemeral=True)
        await interact.followup.send('Você concorda que os seus dados informados acima podem ser disponível publicamente no servidor? (Elas poderão ser excluidas a qualquer momento em que você faça um pedido para a exclusão dos dados digitando `/delete_player`)', ephemeral=True, view=view)


    @app_commands.command()
    @app_commands.describe(invite_link="Link de convite de amizade", username="Nick do jogador")
    async def update_player(self, interact: Interaction, *, invite_link:str = None, username:str = None):
        new_values = {}
        await interact.response.send_message('Atualizando dados do jogador...', ephemeral=True)
        if invite_link:
            new_values["invite_link"] = invite_link
            await interact.followup.send(f'Definindo o seu link de convite de amizade para `{invite_link}`...', ephemeral=True)

        if username:
            new_values["username"] = username 
            await interact.followup.send(f'Definindo o nick para `{username}`...', ephemeral=True)

        result = update_player(interact.guild_id, interact.user.id, new_values)
        await interact.followup.send('Atualização completa!', ephemeral=True)

    @app_commands.command()
    async def player(self, interact: Interaction, member:Member):
        player = get_player(interact.guild_id, member.id)
        if player:
            await interact.response.send_message(str(player))
        else:
            await interact.response.send_message("Este membro não cadastrou seus dados de jogador...")

    @app_commands.command()
    async def delete_player(self, interact: Interaction):
        async def confirm(interact: Interaction):
            response = delete_player(interact.guild_id, interact.user.id)
            await interact.response.send_message('Dados do jogador foi excluido com sucesso!', ephemeral=True)

        async def cancel(interact: Interaction):
            await interact.response.send_message('Ação cancelada!', ephemeral=True)

        view = View()
        yes = Button(label="Sim", style=ButtonStyle.green)
        no = Button(label="Não", style=ButtonStyle.red)

        yes.callback = confirm
        no.callback = cancel

        view.add_item(yes)
        view.add_item(no)
        await interact.response.send_message(f'Tem certeza que quer excluir os seus dados de jogador daqui do servidor?', ephemeral=True, view=view)
    
async def setup(bot):
    await bot.add_cog(ChessPlayer(bot))
