import flet as ft

from utils.functions import FileSingleton

fileSingleton = FileSingleton()


class Logger(ft.ListView):
    def __init__(self, frame, page, **kwargs):
        super().__init__(**kwargs)
        self.FileSingleton = FileSingleton()
        self.data = self.FileSingleton.get_data()
        if "interface" not in self.data:
            self.data["interface"] = {"auto_scroll": True, "auto_refresh": True}
        self.FileSingleton.write_data(self.data)
        self.auto_scroll = self.data["interface"]["auto_scroll"]
        self.limit_logs = self.data["interface"].get("limit_logs", False)

        self.parent = frame
        self.initial_page = page

    def add_text(self, texte: str, color=None):
        text = ft.Text(value=texte, weight=ft.FontWeight.W_600, color=color)

        if self.limit_logs and len(self.controls) > 300:
            self.controls.pop(0)
        self.controls.append(text)
        self.initial_page.update()

    def add_divider(self):
        if self.limit_logs and len(self.controls) > 300:
            self.controls.pop(0)
        self.controls.append(ft.Divider())
        self.initial_page.update()


def get_date():
    pass


class LoggerUpgrade(ft.ListView):
    def __init__(self, page, **kwargs):
        super().__init__(**kwargs)
        data = fileSingleton.get_data()
        if "interface" not in data:
            data["interface"] = {"auto_scroll": True, "auto_refresh": True}
        fileSingleton.write_data(data)
        self.auto_scroll = True
        self.initial_page = page

    def add_text(self, texte: str, color=None):
        if color is None:
            text = ft.Text(value=texte, weight=ft.FontWeight.W_600)
        else:
            text = ft.Text(value=texte, weight=ft.FontWeight.W_600, color=color)
        self.controls.append(text)
        self.initial_page.update()

    def add_divider(self):
        self.controls.append(ft.Divider())
        self.initial_page.update()