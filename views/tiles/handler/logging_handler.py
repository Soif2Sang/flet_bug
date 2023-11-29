import flet as ft


class Logger(ft.ListView):
    def __init__(self, frame, page, **kwargs):
        super().__init__(**kwargs)
        self.auto_scroll = True
        self.initial_page = page

    def add_text(self, texte: str, color=None):
        self.controls.append(ft.Text(value=texte, weight=ft.FontWeight.W_600, color=color))
        self.initial_page.update()

    def add_divider(self):
        self.controls.append(ft.Divider())
        self.initial_page.update()