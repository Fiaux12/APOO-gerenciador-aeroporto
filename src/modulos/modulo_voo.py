import flet as ft
import classes.pessoa.piloto  as piloto
import classes.pessoa.comissario_de_voo  as comissario
from classes.enums.enum_tipo_aviao import EnumTipoAviao
import classes.voo.tripulacao as tripulacao
import classes.pessoa.passageiro as passageiros
import classes.voo.voo as voo
import classes.voo.local as local
import classes.aviao.aviao as aviao

class ModuloVoo():
    def __init__(self) -> None:
        pass

    def cria_voo():
        def button_clicked(e):

            t.update()

        tripulacoes = tripulacao.Tripulacao.carregarListaTripulacao()
        opcoes_tripulacao = [ft.dropdown.Option(f'{tripulacao["id"]}') for _, tripulacao in tripulacoes.iterrows()] if not tripulacoes.empty else []

        avioes = aviao.Aviao.carregarListaAvioes()
        opcoes_avioes = [ft.dropdown.Option(f'{aviao["numero_serie"]}') for _, aviao in avioes.iterrows()] if not avioes.empty else []

        locais = local.Local.carregarListaLocal()
        opcoes_locais = [ft.dropdown.Option(f'{local["cidade"]}') for _, local in locais.iterrows()] if not locais.empty else []

        t = ft.Text()
        texto_tripulacao = ft.Text("Selecione uma tripulação pela identificação", size=15)
        tripulacao_selecionada = ft.Dropdown(width=500, options=opcoes_tripulacao)
        texto_aviao = ft.Text("Selecione um avião pelo número de série", size=15)
        aviao_selecionada = ft.Dropdown(width=500, options=opcoes_avioes)
        texto_origem = ft.Text("Selecione um local de origem pela cidade", size=15)
        origem = ft.Dropdown(width=500, options=opcoes_locais)
        texto_destino = ft.Text("Selecione um local de destino pela cidade", size=15)
        destino = ft.Dropdown(width=500, options=opcoes_locais)

        cadastrar = ft.ElevatedButton(text="Cadastrar", on_click=button_clicked)

        return ft.Column(controls=[texto_tripulacao, tripulacao_selecionada, texto_aviao, aviao_selecionada, texto_origem, origem, texto_destino, destino, cadastrar, t])


    def visualizar_passageiros():
        lista_passageiros = passageiros.Passageiro.carregarListaPassageiros()

        controle_passageiros=[]
        for _, row in lista_passageiros.iterrows():
            controle_passageiros.append(ft.ListTile(title=ft.Text(f'{row["nome"]}, {row["cpf"]}, {row["passaporte"]}'))),
        

        return ft.Column(
            width=500,
            controls=[
                ft.ExpansionTile(
                    title=ft.Text("Passageiros"),
                    affinity=ft.TileAffinity.PLATFORM,
                    subtitle=ft.Text("Nome, CPF, Passaporte"),
                    maintain_state=True,
                    collapsed_text_color=ft.Colors.BLUE,
                    text_color=ft.Colors.BLACK,
                    controls=controle_passageiros,
                )
            ]
        )
    