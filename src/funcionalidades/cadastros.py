import flet as ft

def cadastrar_piloto():
    def button_clicked(e):
        t.value = f"Textboxes values are: '{nome.value}', '{cpf.value}', '{licenca.value}', '{aviao_carga.value}','{aviao_passageiro.value}'."
        t.update()
    
    def aviao_carga_changed(e):
        if aviao_carga.value:
            aviao_passageiro.value = False
            aviao_passageiro.update()

    def aviao_passageiro_changed(e):
        if aviao_passageiro.value:
            aviao_carga.value = False
            aviao_carga.update()

    # TODO: implementar regras para inserir dados
    t = ft.Text()
    nome = ft.TextField(label="Nome")
    cpf = ft.TextField(label="CPF")
    licenca = ft.TextField(label="Número da Licença")

    tipo_aviao = ft.Text("Tipo de avião pilotado", size=15)
    aviao_carga = ft.Checkbox(label="Carga", on_change=aviao_carga_changed)
    aviao_passageiro = ft.Checkbox(label="Passageiro", on_change=aviao_passageiro_changed)

    cadastrar = ft.ElevatedButton(text="Cadastrar", on_click=button_clicked)

    return ft.Column(controls=[nome, cpf, licenca, tipo_aviao, aviao_carga, aviao_passageiro, cadastrar, t])

def cadastrar_comissario():
    def button_clicked(e):
        t.value = f"Textboxes values are: '{nome.value}', '{cpf.value}', '{portugues.value}'."
        t.update()

    # TODO: implementar regras para inserir dados
    t = ft.Text()
    nome = ft.TextField(label="Nome")
    cpf = ft.TextField(label="CPF")
    certificado = ft.TextField(label="Número do Certificado")

    tipo_aviao = ft.Text("Línguas faladas", size=15)
    portugues = ft.Checkbox(label="Português")
    ingues = ft.Checkbox(label="Inglês")
    alemao = ft.Checkbox(label="Alemão")
    russo = ft.Checkbox(label="Russo")
    chines = ft.Checkbox(label="Chinês")
    japones = ft.Checkbox(label="Japonês")
    frances = ft.Checkbox(label="Francês")
    italiano = ft.Checkbox(label="Italiano")


    cadastrar = ft.ElevatedButton(text="Cadastrar", on_click=button_clicked)

    return ft.Column(controls=[nome, cpf, certificado, tipo_aviao, portugues, ingues, alemao, russo, chines, japones, frances, italiano, cadastrar, t])


def cadastrar_aviao():
    def button_clicked(e):
        t.value = f"Textboxes values are: '{capacidade_max.value}', '{velocidade_max.value}', '{qtd_motores.value}'."
        t.update()

    def aviao_carga_changed(e):
        if aviao_carga.value:
            aviao_passageiro.value = False
            aviao_passageiro.update()

    def aviao_passageiro_changed(e):
        if aviao_passageiro.value:
            aviao_carga.value = False
            aviao_carga.update()

    # TODO: implementar regras para inserir dados
    t = ft.Text()
    capacidade_max = ft.TextField(label="Capacidade Máxima")
    velocidade_max = ft.TextField(label="Valocidade Máxima")
    qtd_motores = ft.TextField(label="Número do Motores")
    modelo = ft.TextField(label="Modelo")
    consumo = ft.TextField(label="Consumo em km/h")
    peso_maximo = ft.TextField(label="Peso Máximo")
    serie = ft.TextField(label="Número de Série")

    tipo_aviao = ft.Text("Tipo de avião", size=15)
    aviao_carga = ft.Checkbox(label="Carga", on_change=aviao_carga_changed)
    aviao_passageiro = ft.Checkbox(label="Passageiro", on_change=aviao_passageiro_changed)

    cadastrar = ft.ElevatedButton(text="Cadastrar", on_click=button_clicked)

    return ft.Column(
        controls=[
            capacidade_max,
            velocidade_max, 
            qtd_motores, 
            modelo, 
            consumo, 
            peso_maximo, 
            serie, 
            tipo_aviao,
            aviao_carga,
            aviao_passageiro,
            cadastrar,
            t
        ]
    )

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

                