import flet as ft
import classes.pessoa.piloto  as piloto
from classes.enums.enum_tipo_aviao import EnumTipoAviao

class ModuloPiloto():
    def __init__(self) -> None:
        pass

    def cadastrar_piloto():
        def button_clicked(e):
            tipo_aviao = EnumTipoAviao.CARGA if aviao_carga.value else EnumTipoAviao.PASSAGEIRO
            
            try:
                piloto.Piloto.cadastrar(nome.value, cpf.value, tipo_aviao, licenca.value)
                t.value = f"Piloto {nome.value} cadastrado!"
                t.color = ft.Colors.GREEN

            except Exception as e:
                print(f"An exception occurred: {e}")
                t.value = f"{e}"
                t.color = ft.Colors.RED

            t.update()

        def aviao_carga_changed(e):
            if aviao_carga.value:
                aviao_passageiro.value = False
                aviao_passageiro.update()

        def aviao_passageiro_changed(e):
            if aviao_passageiro.value:
                aviao_carga.value = False
                aviao_carga.update()

        t = ft.Text(size=15)
        nome = ft.TextField(label="Nome", width=500)
        cpf = ft.TextField(label="CPF", width=500)
        licenca = ft.TextField(label="Número da Licença", width=500)

        texto_tipo_aviao = ft.Text("Tipo de avião pilotado", size=15)
        aviao_carga = ft.Checkbox(label="Carga", on_change=aviao_carga_changed)
        aviao_passageiro = ft.Checkbox(label="Passageiro", on_change=aviao_passageiro_changed)

        cadastrar = ft.ElevatedButton(text="Cadastrar", on_click=button_clicked)

        return ft.Column(controls=[nome, cpf, licenca, texto_tipo_aviao, aviao_carga, aviao_passageiro, cadastrar, t])


    def dialog():
        def carregar_lista_pilotos():
            df = piloto.Piloto.carregarListaPilotos()

            rows = []
            for _, row in df.iterrows():
                rows.append([row["nome"], row["cpf"], row["tipo_aviao"], row["numero_licenca"]])

            return rows

        rows = carregar_lista_pilotos()
        dlg = ft.AlertDialog(
            title= ModuloPiloto.pilotosTable(rows), on_dismiss=lambda e: print("Dialog dismissed!")
        )

        def open_dlg(e):
            rows = carregar_lista_pilotos()
            dlg.title = ModuloPiloto.pilotosTable(rows) 
            e.control.page.overlay.append(dlg)
            dlg.open = True
            e.control.page.update()

        return ft.Column(
            [
                ft.ElevatedButton("Visualizar Pilotos", on_click=open_dlg),
            ]
        )

    def pilotosTable(rows):
        return ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Nome")),
                    ft.DataColumn(ft.Text("CPF")),
                    ft.DataColumn(ft.Text("Tipo Avião")),
                    ft.DataColumn(ft.Text("Licença")),
                ],
                rows=[ft.DataRow(cells=[ft.DataCell(ft.Text(cell)) for cell in row]) for row in rows],
            )