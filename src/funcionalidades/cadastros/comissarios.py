import flet as ft

def cadastrar_comissario():
    def button_clicked(e):
        t.value = f"Textboxes values are: '{nome.value}', '{cpf.value}', '{portugues.value}'."
        t.update()

    # TODO: implementar regras para inserir dados
    t = ft.Text()
    nome = ft.TextField(label="Nome", width=500)
    cpf = ft.TextField(label="CPF", width=500)
    certificado = ft.TextField(label="Número do Certificado", width=500)

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

def dialog():
    dlg = ft.AlertDialog(
        title= comissarios(), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def open_dlg(e):
        e.control.page.overlay.append(dlg)
        dlg.open = True
        e.control.page.update()

    return ft.Column(
        [
            ft.ElevatedButton("Visualizar comissarios", on_click=open_dlg),
        ]
    )

def comissarios():
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