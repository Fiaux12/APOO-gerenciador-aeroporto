import flet as ft
import classes.pessoa.piloto  as piloto
import classes.pessoa.comissario_de_voo  as comissario
from classes.enums.enum_tipo_aviao import EnumTipoAviao
import classes.voo.tripulacao as tripulacao
import classes.pessoa.passageiro as passageiros
import classes.voo.voo as voo
import classes.voo.local as local
import classes.aviao.aviao as aviao
import asyncio

class ModuloVoo():
    def __init__(self) -> None:
        pass

    def visualizar_voos():
        lista_passageiros = passageiros.Passageiro.carregarListaPassageiros()


        controle_passageiros=[]
        for _, row in lista_passageiros.iterrows():
            controle_passageiros.append(ft.ListTile(title=ft.Text(f'{row["nome"]}, {row["cpf"]}, {row["passaporte"]}'))),
        
        
        rows = ModuloVoo.carregar_lista_voos()
        tabela = ModuloVoo.voosTable(rows)

        lista_passageiros = ft.ExpansionTile(
                    title=ft.Text("Passageiros do voo"),
                    affinity=ft.TileAffinity.PLATFORM,
                    subtitle=ft.Text("Nome, CPF, Passaporte"),
                    maintain_state=True,
                    collapsed_text_color=ft.Colors.BLUE,
                    text_color=ft.Colors.BLACK,
                    controls=controle_passageiros,
                ),

        return ft.Column(
            controls=[
                tabela
            ]
        )
    
    def carregar_lista_voos():
            df = voo.Voo.carregarListaVoos()

            rows = []
            for _, row in df.iterrows():
                duracao_arredondada = str(round(row["duracao_estimada"], 2))

                rows.append([
                    row["aviao"],
                    row["tripulacao_id"],
                    row["origem"],
                    row["destino"],
                    duracao_arredondada+" h",  
                    row["saida"].replace("-", "/").replace("T", "-"),
                    row["chegada"].replace("-", "/").replace("T", "-"),
                    row["status"],
                ])

            return rows
    
    def voosTable(rows):
        return ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Avião")),
                    ft.DataColumn(ft.Text("Tripulação")),
                    ft.DataColumn(ft.Text("Cidade de Origem")),
                    ft.DataColumn(ft.Text("Cidade do Destino")),
                    ft.DataColumn(ft.Text("Duração Estimada")),
                    ft.DataColumn(ft.Text("Data de Saída")),
                    ft.DataColumn(ft.Text("Data de Chegada")),
                    ft.DataColumn(ft.Text("Status")),
                ],
                rows=[ft.DataRow(cells=[ft.DataCell(ft.Text(cell)) for cell in row]) for row in rows],
            )
    