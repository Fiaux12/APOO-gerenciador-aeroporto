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


    if aviao_carga.value == True:
        aviao_passageiro.value = False

    if aviao_passageiro.value == True:
        aviao_carga.value = False

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
