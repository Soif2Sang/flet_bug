import flet as ft

from utils.flet_translations import translate
from utils.functions import FileSingleton
from views.settings.general.Flet_general_settings import InterfaceSettings
from views.settings.profile.profile import SettingContainer
from views.tiles.handler.logging_handler import Logger

color_bank = {1: "#3b8ed0", 2: "#ba4543", 3: "#dec433"}


class Frame(ft.Tabs):
    def __init__(self, page, number: str, **kwargs):
        super().__init__(**kwargs)
        self.number = number
        self.settings = ft.Tabs()
        self.expand = True
        self.initial_page = page
        self.logger = Logger(self, page)

        self.tabs.append(ft.Tab(content=self.logger, text=translate("Logs")))
        self.tabs.append(ft.Tab(content=self.settings, text=translate("Settings")))
        self.tabs.append(InterfaceSettings(page, number))
        #
        # self.settings.tabs.append(ft.Tab(content=ProfileSettings(page, self, number, 1), text=translate("Profile 1")))
        # self.settings.tabs.append(ft.Tab(content=ProfileSettings(page, self, number, 2), text=translate("Profile 2")))
        # self.settings.tabs.append(ft.Tab(content=ProfileSettings(page, self, number, 3), text=translate("Profile 3")))

        self.settings.tabs.append(
            ft.Tab(
                content=SettingContainer(page, number, 1), text=translate("Profile 1")
            )
        )
        self.settings.tabs.append(
            ft.Tab(
                content=SettingContainer(page, number, 2), text=translate("Profile 2")
            )
        )
        self.settings.tabs.append(
            ft.Tab(
                content=SettingContainer(page, number, 3), text=translate("Profile 3")
            )
        )

        self.FileSingleton = FileSingleton()

        data = self.FileSingleton.get_data()
        for profile in data[str(number)]["schedules"]:
            if data[str(number)]["schedules"][profile]["enabled"]:
                self.settings.selected_index = int(profile) - 1
                break

    def add_text(self, texte: str, color=None):
        self.logger.add_text(texte, color)

    def add_divider(self):
        self.logger.add_divider()


class FrameUpgrade(ft.Tabs):
    def __init__(self, page, number: str, **kwargs):
        super().__init__(**kwargs)
        self.initial_page = page
        self.number = number
        self.settings = ft.Tabs()
        self.expand = True
        self.width = 400
        self.logger = self.initial_page.logger
        self.FileSingleton = FileSingleton()

        self.tabs.append(ft.Tab(content=self.settings, text=translate("Settings")))
        self.tabs.append(ft.Tab(content=self.logger, text=translate("Logs")))
        self.tabs.append(InterfaceSettings(page, number))
        # self.settings.tabs.append(ft.Tab(content=ProfileSettings(page, self, int(number), 1), text="Profile 1"))
        # self.settings.tabs.append(ft.Tab(content=ProfileSettings(page, self, int(number), 2), text="Profile 2"))
        # self.settings.tabs.append(ft.Tab(content=ProfileSettings(page, self, int(number), 3), text="Profile 3"))

        self.settings.tabs.append(
            ft.Tab(content=SettingContainer(page, number, 1), text="Profile 1")
        )
        self.settings.tabs.append(
            ft.Tab(content=SettingContainer(page, number, 2), text="Profile 2")
        )
        self.settings.tabs.append(
            ft.Tab(content=SettingContainer(page, number, 3), text="Profile 3")
        )

        data = self.FileSingleton.get_data()
        for profile in data[str(number)]["schedules"]:
            # print(self.settings.selected_index)
            if data[str(number)]["schedules"][profile]["enabled"]:
                self.settings.selected_index = int(profile) - 1
                break

    def add_text(self, texte: str):
        self.logger.add_text(texte)
