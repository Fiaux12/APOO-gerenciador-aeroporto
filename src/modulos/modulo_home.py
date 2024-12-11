import flet as ft

class ModuloHome():
    def __init__(self) -> None:
        pass


    def home():

        return ft.Column(
            controls=[
                ft.Text("Bem vindo!", size=30),
                ft.Text("Bem-vindo ao Gerenciador de Voos: eficiência e segurança para conectar destinos.", size=20),
                ft.Text("Faça  o cadastro dos pilotos e dos comissários de bordo para criar uma tripulação."),
                ft.Text("Faça o cadastro dos aviões na aba, Aviões."),
                ft.Text("Crie um voo com os dados criados e com os dados da nossa base de dados"),
            ]
        )