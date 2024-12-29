import flet as ft
import modulos.modulo_piloto as modulo_piloto
import modulos.modulo_comissarios  as modulo_comissarios
import modulos.modulo_tripulacao  as modulo_tripulacao
import modulos.modulo_aviao  as modulo_aviao
import modulos.modulo_home  as modulo_home
import modulos.modulo_criar_voo as modulo_criar_voo
import modulos.modulo_voo as modulo_voo

# class Gerenciador():
#     def __init__(self) -> None:
#         Gerenciador.main()

def update_content(index, body_content):
    body_content.controls.clear() 

    if index == 0: 
        body_content.controls.append(modulo_home.ModuloHome.home())
        
    if index == 1: 
        body_content.controls.append(ft.Text("Pilotos", size=20))
        body_content.controls.append(modulo_piloto.ModuloPiloto.dialog())
        body_content.controls.append(ft.Divider())
        body_content.controls.append(ft.Text("Cadastrar Pilotos", size=20))
        body_content.controls.append(modulo_piloto.ModuloPiloto.cadastrar_piloto())

    elif index == 2: 
        body_content.controls.append(ft.Text("Comissários", size=20))
        body_content.controls.append(modulo_comissarios.ModuloComissario.dialog())
        body_content.controls.append(ft.Divider())
        body_content.controls.append(ft.Text("Cadastrar Comissários", size=20))
        body_content.controls.append(modulo_comissarios.ModuloComissario.cadastrar_comissario())

    elif index == 3:  
        body_content.controls.append(ft.Text("Tripulação", size=20))
        body_content.controls.append(modulo_tripulacao.ModuloTripulacao.dialog())
        body_content.controls.append(ft.Divider())
        body_content.controls.append(modulo_tripulacao.ModuloTripulacao.criar_tripulacao())

    elif index == 4: 
        body_content.controls.append(ft.Text("Aviões", size=20))
        body_content.controls.append(modulo_aviao.ModuloAviao.dialog())
        body_content.controls.append(ft.Divider())
        body_content.controls.append(ft.Text("Cadastrar Aviões", size=20))
        body_content.controls.append(modulo_aviao.ModuloAviao.cadastrar_aviao())

    elif index == 5:  
        body_content.controls.append(ft.Text("Criar Voo", size=20))
        body_content.controls.append(ft.Divider())
        body_content.controls.append(modulo_criar_voo.ModuloCriarVoo.cria_voo())

    elif index == 6:  
        body_content.controls.append(ft.Text("Visualizar Voos", size=20))
        body_content.controls.append(ft.Divider())
        body_content.controls.append(modulo_voo.ModuloVoo.visualizar_voos())

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
    body_content.controls.append(modulo_home.ModuloHome.home())

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
                icon=ft.Icons.MY_LIBRARY_ADD_OUTLINED, selected_icon=ft.Icons.MY_LIBRARY_ADD_ROUNDED, label="Criar Voo"
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
