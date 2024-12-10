import flet as ft
import classes.pessoa.piloto  as piloto
import classes.pessoa.comissario_de_voo  as comissario
from classes.enums.enum_tipo_aviao import EnumTipoAviao
import classes.voo.tripulacao as tripulacao


def criar_tripulacao():
    def button_clicked(e):
        piloto_selecionado_str = f"Pilotos selecionados: {piloto_selecionado_1.value}, {piloto_selecionado_2.value}\n"
        comissarios_selecionados = [
            dropdown.value for dropdown in dropdowns_comissarios if dropdown.value
        ]
        comissarios_selecionados_str = f"Comissários selecionados: {', '.join(comissarios_selecionados)}"
        t.value = piloto_selecionado_str + comissarios_selecionados_str
        t.update()

        tripulacao.Tripulacao.contruir_tripulacao(piloto_selecionado_1.value, piloto_selecionado_2.value, comissarios_selecionados)

    pilotos = piloto.Piloto.carregarListaPilotos()
    opcoes_pilotos = [ft.dropdown.Option(piloto["nome"]) for _, piloto in pilotos.iterrows()] if not pilotos.empty else []

    comissarios = comissario.ComissarioDeVoo.carregarListaComissarios()
    opcoes_comissarios = [ft.dropdown.Option(comissario["nome"]) for _, comissario in comissarios.iterrows()] if not comissarios.empty else []

    dropdowns_comissarios = []

    def atualizar_comissarios(e):
        quantidade = int(numero_comissarios.value) if numero_comissarios.value else 0
        lista_comissarios.controls.clear()
        dropdowns_comissarios.clear()
        lista_comissarios.controls.append(ft.Text("Selecione os comissários", size=15))
        for i in range(quantidade):
            dropdown = ft.Dropdown(
                width=500,
                options=opcoes_comissarios,
                hint_text=f"Comissário {i + 1}"
            )
            dropdowns_comissarios.append(dropdown)
            lista_comissarios.controls.append(dropdown)
        lista_comissarios.update()

    t = ft.Text()
    texto_piloto_1 = ft.Text("Selecione o piloto principal", size=15)
    piloto_selecionado_1 = ft.Dropdown(width=500, options=opcoes_pilotos)

    texto_piloto_2 = ft.Text("Selecione o copiloto", size=15)
    piloto_selecionado_2 = ft.Dropdown(width=500, options=opcoes_pilotos)

    texto_numero_comissarios = ft.Text("Selecione o número de comissários", size=15)
    numero_comissarios = ft.Dropdown(
        width=100,
        options=[ft.dropdown.Option(str(i)) for i in range(1, 11)],
        on_change=atualizar_comissarios
    )

    lista_comissarios = ft.Column()

    return ft.Column(controls=[
        texto_piloto_1,
        piloto_selecionado_1,
        texto_piloto_2,
        piloto_selecionado_2,
        texto_numero_comissarios,
        numero_comissarios,
        lista_comissarios,
        ft.ElevatedButton(text="Submit", on_click=button_clicked),
        t
    ])

