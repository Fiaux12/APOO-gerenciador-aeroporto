import datetime
import flet as ft

class InputData(ft.Column):
    def __init__(self):
        super().__init__()

        self.datepicker = ft.DatePicker(
            first_date=datetime.datetime(2024, 10, 1),
            last_date=datetime.datetime(2027, 12, 1),
            on_change=self.change_date,
            confirm_text="Ok",
            cancel_text="Cancelar",
            error_invalid_text="Data inválida",
            field_label_text="Data de Saída",
            field_hint_text="Data de Saída",
            help_text="Data de Saída"
        )

        self.selected_date = ft.Text()  

        self.controls = [
            ft.ElevatedButton(
                "Data de saída",
                icon=ft.Icons.CALENDAR_MONTH,
                on_click=self.open_date_picker,
            ),
            self.selected_date,
        ]

    def open_date_picker(self, e):
        self.datepicker.pick_date()

    def change_date(self, e):
        self.selected_date.value = f"Data de Saída: {self.datepicker.value}"
        self.page.update()

    def did_mount(self):
        self.page.overlay.append(self.datepicker)
        self.page.update()

    def will_unmount(self):
        self.page.overlay.remove(self.datepicker)
        self.page.update()


    