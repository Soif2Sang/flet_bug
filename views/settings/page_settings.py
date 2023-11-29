import flet as ft
from flet_core import ButtonStyle, RoundedRectangleBorder

from utils.functions import FileSingleton

color_bank = {1: "#3b8ed0", 2: "#ba4543", 3: "#dec433"}


class PageSettings(ft.Container):
    def __init__(self, page, instance_index: str, profile_index: int):
        super().__init__()
        self.FileSingleton = FileSingleton()
        self.data = self.FileSingleton.get_data()
        self.initial_page = page
        self.instance_index = instance_index
        self.profile_index = profile_index
        self.padding = ft.padding.only(top=5, left=0, bottom=0)
        self.content: ft.ListView = ft.ListView(
            height=400, expand=1, padding=1, spacing=6
        )

        self.theme = ft.Theme(
            color_scheme=ft.ColorScheme(primary=color_bank[self.profile_index])
        )
        self.init()

    def add(self, *control):
        for ctrl in control:
            self.content.controls.append(ctrl)

    def goBack(self):
        self.content.controls = []
        self.data = self.FileSingleton.get_data()
        self.init()
        self.initial_page.update()

    def init(self):
        pass
