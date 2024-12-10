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
    nome = ft.TextField(label="Nome", width=500)
    cpf = ft.TextField(label="CPF", width=500)
    licenca = ft.TextField(label="Número da Licença", width=500)

    tipo_aviao = ft.Text("Tipo de avião pilotado", size=15)
    aviao_carga = ft.Checkbox(label="Carga", on_change=aviao_carga_changed)
    aviao_passageiro = ft.Checkbox(label="Passageiro", on_change=aviao_passageiro_changed)

    cadastrar = ft.ElevatedButton(text="Cadastrar", on_click=button_clicked)

    return ft.Column(controls=[nome, cpf, licenca, tipo_aviao, aviao_carga, aviao_passageiro, cadastrar, t])


def dialog():
    dlg = ft.AlertDialog(
        title= pilotos(), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def open_dlg(e):
        e.control.page.overlay.append(dlg)
        dlg.open = True
        e.control.page.update()

    return ft.Column(
        [
            ft.ElevatedButton("Visualizar Pilotos", on_click=open_dlg),
        ]
    )

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