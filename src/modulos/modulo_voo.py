import flet as ft
import classes.pessoa.piloto  as piloto
import classes.pessoa.comissario_de_voo  as comissario
from classes.enums.enum_tipo_aviao import EnumTipoAviao
import classes.voo.tripulacao as tripulacao
import classes.pessoa.passageiro as passageiros

class ModuloVoo():
    def __init__(self) -> None:
        pass
    

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
    