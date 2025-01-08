import flet as ft
import classes.pessoa.passageiro as passageiros
from classes.voo.tripulacao import Tripulacao
import classes.voo.voo as voo

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
        def on_cell_click(e):
            tripulacao_id = e.control.data
            tripulacao = Tripulacao.getTripulacaoById(tripulacao_id)
            detalhes_tripulacao = f"Número da tripulação {tripulacao_id}:\n\n"

            detalhes_tripulacao += "Pilotos:\n"
            for piloto in tripulacao["pilotos"]:
                nome, registro = piloto.split(", ")
                detalhes_tripulacao += f" - Nome: {nome}, CPF: {registro}\n"

            detalhes_tripulacao += "\nComissários de Voo:\n"
            for comissario in tripulacao["comissarios_voo"]:
                nome, registro = comissario.split(", ")
                detalhes_tripulacao += f" - Nome: {nome}, CPF: {registro}\n"


            def close_dialog(e):
                dlg.open = False
                e.page.update()
            
            dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Detalhes da Tripulação"),
                content=ft.Text(detalhes_tripulacao),
                actions=[
                    ft.TextButton("Fechar", on_click=close_dialog),
                ]
            )
            
            e.page.dialog = dlg
            dlg.open = True
            e.page.update()

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
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(cell)) if i != 1 else ft.DataCell(
                            ft.ElevatedButton(
                                text="Detalhes",
                                data=row[1],  # Passa o id da tripulação
                                on_click=on_cell_click, 
                            )
                        )
                        for i, cell in enumerate(row)
                    ]
                )
                for row in rows
            ],
        )
