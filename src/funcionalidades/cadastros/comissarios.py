import flet as ft
import classes.pessoa.comissario_de_voo  as comissario


def cadastrar_comissario():
    def button_clicked(e):
        
        linguas_selecionadas = [lingua.label for lingua in lista_linguas if lingua.value]
        comissario.ComissarioDeVoo.cadastrar(nome.value, cpf.value, linguas_selecionadas, certificado.value)

        t.value = f"Nome: {nome.value}, CPF: {cpf.value}, Línguas: {', '.join(linguas_selecionadas)}."
        t.update()

    t = ft.Text()
    nome = ft.TextField(label="Nome", width=500)
    cpf = ft.TextField(label="CPF", width=500)
    certificado = ft.TextField(label="Número do Certificado", width=500)

    texto_linguas = ft.Text("Línguas faladas", size=15)
    linguas = ['Português', 'Inglês', 'Alemão', 'Russo', 'Chinês', 'Japonês', 'Francês', 'Italiano']
    lista_linguas = [ft.Checkbox(label=lingua) for lingua in linguas]
    cadastrar = ft.ElevatedButton(text="Cadastrar", on_click=button_clicked)

    return ft.Column(controls=[nome, cpf, certificado, texto_linguas] + lista_linguas + [cadastrar, t])

def dialog():
    def carregar_lista_comissarios():
        df = comissario.ComissarioDeVoo.carregarListaComissarios()

        rows = []
        for _, row in df.iterrows():
            linguas_str = ', '.join(row["linguas"]) 
            rows.append([row["nome"], row["cpf"], linguas_str, row["numero_certificado"]])
        
        return rows

    rows = carregar_lista_comissarios()
    dlg = ft.AlertDialog(
        title=comissarios(rows), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def open_dlg(e):
        rows = carregar_lista_comissarios()
        dlg.title = comissarios(rows) 
        e.control.page.overlay.append(dlg)
        dlg.open = True
        e.control.page.update()

    return ft.Column(
        [
            ft.ElevatedButton("Visualizar Comissarios", on_click=open_dlg),
        ]
    )

def comissarios(rows):
    return ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Nome")),
                ft.DataColumn(ft.Text("CPF")),
                ft.DataColumn(ft.Text("Linguas Faladas")),
                ft.DataColumn(ft.Text("Certificado")),
            ],
            rows=[ft.DataRow(cells=[ft.DataCell(ft.Text(cell)) for cell in row]) for row in rows],
        )