import flet as ft
import funcionalidades.cadastros.piloto  as piloto
import funcionalidades.cadastros.comissarios  as comissarios
import funcionalidades.cadastros.tripulacao  as tripulacao
import funcionalidades.cadastros.aviao  as aviao
import funcionalidades.home  as home

def update_content(index, body_content):
    body_content.controls.clear() 

    if index == 0: 
        body_content.controls.append(home.home())
        
    if index == 1: 
        body_content.controls.append(ft.Text("Pilotos", size=20))
        body_content.controls.append(piloto.dialog())
        body_content.controls.append(ft.Divider())
        body_content.controls.append(ft.Text("Cadastrar Pilotos", size=20))
        body_content.controls.append(piloto.cadastrar_piloto())


    elif index == 2: 
        body_content.controls.append(ft.Text("Comissários", size=20))
        body_content.controls.append(comissarios.dialog())
        body_content.controls.append(ft.Divider())
        body_content.controls.append(ft.Text("Cadastrar Comissários", size=20))
        body_content.controls.append(comissarios.cadastrar_comissario())

    elif index == 3:  
        body_content.controls.append(ft.Text("Tripulação", size=20))
        body_content.controls.append(tripulacao.dialog())
        body_content.controls.append(ft.Divider())
        body_content.controls.append(tripulacao.criar_tripulacao())

    elif index == 4: 
        body_content.controls.append(ft.Text("Aviões", size=20))
        body_content.controls.append(aviao.dialog())
        body_content.controls.append(ft.Divider())
        body_content.controls.append(ft.Text("Cadastrar Aviões", size=20))
        body_content.controls.append(aviao.cadastrar_aviao())


    elif index == 5:  
        body_content.controls.append(ft.Text("Criar Voo", size=20))

    body_content.update() 

def main(page: ft.Page):
    page.title = "Gerenciador de Voos"
    page.window.width = 1300
    page.window.height = 700
    page.scroll = "none"  
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.update()

    body_content = ft.Column(
        alignment=ft.MainAxisAlignment.START,
        expand=True,
        scroll="adaptive",  
    )
    body_content.controls.append(home.home())

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.HOME_OUTLINED, selected_icon=ft.Icons.HOME_ROUNDED, label="Home"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.PERSON_4_OUTLINED, selected_icon=ft.Icons.PERSON_4_ROUNDED, label="Pilotos"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.PERSON_3_OUTLINED, selected_icon=ft.Icons.PERSON_3_ROUNDED, label="Comissários"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.GROUPS_3_OUTLINED, selected_icon=ft.Icons.GROUPS_3_ROUNDED, label="Tripulação"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.FLIGHT_OUTLINED, selected_icon=ft.Icons.FLIGHT, label="Aviões"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.FLIGHT_TAKEOFF_OUTLINED, selected_icon=ft.Icons.FLIGHT_TAKEOFF, label="Voos"
            ),
        ],
        on_change=lambda e: update_content(e.control.selected_index, body_content),
    )

    layout = ft.Row(
        [
            rail, 
            ft.VerticalDivider(width=1),
            ft.Container(
                content=body_content,
                expand=True,  
            ),
        ],
        expand=True,  
    )

    page.add(layout)
    page.update()


ft.app(target=main)
