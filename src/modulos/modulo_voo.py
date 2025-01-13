import flet as ft
from classes.enums.enum_status_voo import EnumStatusVoo
from classes.voo.tripulacao import Tripulacao
import classes.voo.voo as voo

class ModuloVoo():

    #Container da tabela
    tabela_container = ft.Container()

    def __init__(self) -> None:
        pass

    def atualizar_tabela():
            rows = ModuloVoo.carregar_lista_voos()
            ModuloVoo.tabela_container.content = ModuloVoo.voosTable(rows)

    def visualizar_voos():
        # lista_passageiros = passageiros.Passageiro.carregarLista()

        # controle_passageiros = []
        # for _, row in lista_passageiros.iterrows():
        #     controle_passageiros.append(ft.ListTile(title=ft.Text(f'{row["nome"]}, {row["cpf"]}, {row["passaporte"]}'))),

        # lista_passageiros = ft.ExpansionTile(
        #     title=ft.Text("Passageiros do voo"),
        #     affinity=ft.TileAffinity.PLATFORM,
        #     subtitle=ft.Text("Nome, CPF, Passaporte"),
        #     maintain_state=True,
        #     collapsed_text_color=ft.Colors.BLUE,
        #     text_color=ft.Colors.BLACK,
        #     controls=controle_passageiros,
        # )
        ModuloVoo.atualizar_tabela()

        return ft.Column(
            controls=[
                ModuloVoo.tabela_container  
            ]
        )

    
    def carregar_lista_voos():
            df = voo.Voo.carregarListaVoos()

            rows = []
            for _, row in df.iterrows():
                duracao_horas = int(row["duracao_estimada"])
                duracao_minutos = int((row["duracao_estimada"] - duracao_horas) * 60)
                duracao_formatada = f"{duracao_horas}h {duracao_minutos} min"

                rows.append([
                    row["aviao"],
                    row["tripulacao_id"],
                    row["origem"],
                    row["destino"],
                    duracao_formatada,  
                    row["saida"].replace("-", "/").replace("T", "-"),
                    row["chegada"].replace("-", "/").replace("T", "-"),
                    row["status"],
                    row["id"],
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

        def on_cell_click_status(e):
            id_voo = e.control.data
            opcoes_status = [
                ft.dropdown.Option(EnumStatusVoo.PLANEJADO.value),
                ft.dropdown.Option(EnumStatusVoo.CONFIRMADO.value),
                ft.dropdown.Option(EnumStatusVoo.EMBARQUE.value),
                ft.dropdown.Option(EnumStatusVoo.EM_VOO.value),
                ft.dropdown.Option(EnumStatusVoo.FINALIZADO.value),
                ft.dropdown.Option(EnumStatusVoo.CANCELADO.value),
            ] 
            status_selecionado = ft.Dropdown(width=500, options=opcoes_status)

            def close_dialog(e):
                if status_selecionado.value != None:
                    voo.Voo.atualizar_status_voo(status_selecionado.value, id_voo)
                ModuloVoo.atualizar_tabela()

                dlg.open = False
                e.page.update()
            
            dlg = ft.AlertDialog(
                modal=True,
                title=ft.Text("Alterar status do voo"),
                content=status_selecionado,
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
                ft.DataColumn(ft.Text("ID"), visible=False),  # Torna a coluna do ID invisível
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(cell)) if i != 1 and i != 7 and i != 8 else
                        ft.DataCell(
                            ft.ElevatedButton(
                                text="Detalhes",
                                data=row[1],  # Tripulação ID
                                on_click=on_cell_click,
                            )
                        ) if i == 1 else
                        ft.DataCell(
                            ft.ElevatedButton(
                                text=str(cell),  # Texto do botão é o status
                                data=row[8],  # Passa o ID do voo para ser usado no on_click
                                on_click=on_cell_click_status,
                            )
                        ) if i == 7 else
                        ft.DataCell(ft.Text(""), visible=False)  # Oculta o ID
                        for i, cell in enumerate(row)
                    ]
                )
                for row in rows
            ],
        )