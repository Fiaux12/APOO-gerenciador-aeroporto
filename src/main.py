import flet as ft

def pilotos():
    return ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Nome")),
                ft.DataColumn(ft.Text("CPF")),
                ft.DataColumn(ft.Text("Gênero")),
                ft.DataColumn(ft.Text("Licença")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("João Ribeiro")),
                        ft.DataCell(ft.Text("456.789.321-85")),
                        ft.DataCell(ft.Text("Masculino")),
                        ft.DataCell(ft.Text("Carga")),
                    ]
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Clarice Romano")),
                        ft.DataCell(ft.Text("782.663.751-28")),
                        ft.DataCell(ft.Text("Feminino")),
                        ft.DataCell(ft.Text("Passageiro")),
                    ]
                )
            ]
        )

def main(page: ft.Page):
    # add controles da pagina
    page.title = "Gerenciador de Voos"
    page.window_width = 1300
    page.window_height = 700

    page.scroll = "adaptative"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.update()

    rail = ft.NavigationRail(
        selected_index = 0,
        label_type = ft.NavigationRailLabelType.ALL,
        min_width = 100,
        min_extended_width = 400,
        # leading = ft.FloatingActionButton(icon=ft.icons.CREATE, text="Add"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.PERSON_4_OUTLINED, selected_icon=ft.icons.PERSON_4_ROUNDED, label="Cadastrar Pilotos"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.PERSON_3_OUTLINED, selected_icon=ft.icons.PERSON_3_ROUNDED, label="Cadastrar Comissarios"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.GROUPS_3_OUTLINED, selected_icon=ft.icons.GROUPS_3_ROUNDED, label="Criar Tripulaçao"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.FLIGHT_OUTLINED, selected_icon=ft.icons.FLIGHT, label="Cadastrar Aviões"
            ),
            ft.NavigationRailDestination(
                icon=ft.icons.FLIGHT_TAKEOFF_OUTLINED, selected_icon=ft.icons.FLIGHT_TAKEOFF, label="Criar Voo"
            ),
        ],
        on_change=lambda e: print("selected destinacion:", e.control.selected_index),
    )

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column([ft.Text("body!")], alignment=ft.MainAxisAlignment.START,expand=True),
            ],
            width=1300,
            height=700,

        )
    )

    # page.add(
    #     ft.Text("Cadastrar Tripulação", size=30, theme_style= ft.TextThemeStyle.HEADLINE_SMALL),
    #     ft.Text("Criar Novos Voos", size=30, theme_style= ft.TextThemeStyle.HEADLINE_SMALL),
    #     ft.Text("Visualizar Voos", size=30, theme_style= ft.TextThemeStyle.HEADLINE_SMALL),
    # )
    # page.add(pilotos())

    page.update()

ft.app(target=main)
