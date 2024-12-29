import flet as ft

class InputTempo(ft.Column):
    def __init__(self):
        super().__init__()
        self.timepicker = ft.TimePicker(
            confirm_text="Ok",
            cancel_text="Cancelar",
            error_invalid_text="Tempo fora do intervalo",
            help_text="Escolha um horário",
            hour_label_text="Hora",
            minute_label_text="Minutos",
            on_change=self.change_time,
        )
        self.selected_time = ft.Text()

        self.controls = [
            ft.ElevatedButton(
                "Horário de saída",
                icon=ft.Icons.CALENDAR_MONTH,
                on_click=self.open_time_picker,
            ),
            self.selected_time,
        ]

    def open_time_picker(self, e):
        e.control.page.open(self.timepicker)

    def change_time(self, e):
        self.selected_time.value = f"Selecione o horário: {self.timepicker.value}"
        e.control.page.update()

    def did_mount(self):
        self.page.overlay.append(self.timepicker)
        self.page.update()

    def will_unmount(self):
        self.page.overlay.remove(self.timepicker)
        self.page.update()