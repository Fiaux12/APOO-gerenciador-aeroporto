import flet as ft

class ModuloHome():
    def __init__(self) -> None:
        pass

    def home():

        return ft.Column(
            controls=[
                ft.Text("Gerenciador de Voos", size=30),
                ft.Text("Bem-vindo ao Gerenciador de Voos: eficiência e segurança para conectar destinos.", size=20),
                ft.Text("Comece cadastrando os pilotos e os comissários de bordo para formar a tripulação necessária para os voos."),
                ft.Text("Na aba 'Aviões', você pode cadastrar os aviões disponíveis para os voos."),
                ft.Text("Crie e gerencie voos com os dados já cadastrados, e acompanhe tudo na aba 'Voos'."),
                ft.Text("Atualize o status dos voos conforme eles progridem, garantindo o acompanhamento em tempo real."),
            ]
        )