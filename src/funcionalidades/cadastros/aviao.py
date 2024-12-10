import flet as ft

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
    capacidade_max = ft.TextField(label="Capacidade Máxima", width=500)
    velocidade_max = ft.TextField(label="Valocidade Máxima", width=500)
    qtd_motores = ft.TextField(label="Número do Motores", width=500)
    modelo = ft.TextField(label="Modelo", width=500)
    consumo = ft.TextField(label="Consumo em km/h", width=500)
    peso_maximo = ft.TextField(label="Peso Máximo", width=500)
    serie = ft.TextField(label="Número de Série", width=500)

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


def dialog():
    dlg = ft.AlertDialog(
        title= avioes(), on_dismiss=lambda e: print("Dialog dismissed!")
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

def avioes():
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