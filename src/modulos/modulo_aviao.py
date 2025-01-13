import flet as ft
import classes.aviao.aviao  as aviao
import classes.aviao.aviao_carga  as aviao_carga_class
import classes.aviao.aviao_passageiro  as aviao_passageiro_class
from classes.enums.enum_tipo_aviao import EnumTipoAviao

class ModuloAviao():
    def __init__(self) -> None:
        pass

    def cadastrar_aviao():
        def button_clicked(e):

            tipo_aviao = None
            if aviao_carga.value != False and aviao_passageiro != False:
                tipo_aviao = EnumTipoAviao.CARGA if aviao_carga.value else EnumTipoAviao.PASSAGEIRO

            try:
                
                if aviao_carga.value:
                    aviao_carga_class.AviaoCarga.cadastrar(
                        capacidade_max.value,
                        velocidade_max.value, 
                        qtd_motores.value, 
                        modelo.value, 
                        consumo.value, 
                        peso_maximo.value, 
                        serie.value,
                        tipo_aviao
                    )
                else:
                    aviao_passageiro_class.AviaoPassageiro.cadastrar(
                        capacidade_max.value,
                        velocidade_max.value, 
                        qtd_motores.value, 
                        modelo.value, 
                        consumo.value, 
                        peso_maximo.value, 
                        serie.value,
                        tipo_aviao
                    )

                t.value = f"Avião {serie.value} cadastrado!"
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

        t = ft.Text()
        serie = ft.TextField(label="Número de Série", width=500)
        modelo = ft.TextField(label="Modelo", width=500)
        capacidade_max = ft.TextField(label="Capacidade Máxima (t)", width=500)
        velocidade_max = ft.TextField(label="Valocidade Máxima (km/h)", width=500)
        qtd_motores = ft.TextField(label="Número do Motores", width=500)
        consumo = ft.TextField(label="Consumo (l/km)", width=500)
        peso_maximo = ft.TextField(label="Peso Máximo (t)", width=500)

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
        def carregar_lista_avioes():
            df = aviao.Aviao.carregarLista()

            rows = []
            for _, row in df.iterrows():
                rows.append([
                    row["numero_serie"],
                    row["modelo"],
                    row["tipo"],
                    row["capacidade_maxima"],
                    row["velocidade_maxima"],
                    row["qtd_motores"],
                    row["consumo"],
                    row["peso_maximo"],
                ])

            return rows

        rows = carregar_lista_avioes()
        dlg = ft.AlertDialog(
            title=ModuloAviao.avioesTable(rows), on_dismiss=lambda e: print("Dialog dismissed!")
        )

        def open_dlg(e):
            rows = carregar_lista_avioes()
            dlg.title = ModuloAviao.avioesTable(rows) 
            e.control.page.overlay.append(dlg)
            dlg.open = True
            e.control.page.update()

        return ft.Column(
            [
                ft.ElevatedButton("Visualizar Aviões", on_click=open_dlg),
            ]
        )

    def avioesTable(rows):
        return ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("Número de Série")),
                    ft.DataColumn(ft.Text("Modelo")),
                    ft.DataColumn(ft.Text("Tipo")),
                    ft.DataColumn(ft.Text("Capacidade Máxima")),
                    ft.DataColumn(ft.Text("Valocidade Máxima")),
                    ft.DataColumn(ft.Text("Número do Motores")),
                    ft.DataColumn(ft.Text("Consumo em l/km")),
                    ft.DataColumn(ft.Text("Peso Máximo")),
                ],
                rows=[ft.DataRow(cells=[ft.DataCell(ft.Text(cell)) for cell in row]) for row in rows],
            )