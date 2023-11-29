import flet as ft

from utils.flet_translations import translate
from views.tiles.handler.logging_handler import Logger

color_bank = {1: "#3b8ed0", 2: "#ba4543", 3: "#dec433"}


class Frame(ft.Tabs):
    def __init__(self, page, number: str, **kwargs):
        super().__init__(**kwargs)
        self.number = number
        self.expand = True
        self.initial_page = page
        self.logger = Logger(self, page)

        self.tabs.append(ft.Tab(content=self.logger, text=translate("Logs")))


    def add_text(self, texte: str, color=None):
        self.logger.add_text(texte, color)

    def add_divider(self):
        self.logger.add_divider()
