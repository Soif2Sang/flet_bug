import flet as ft

from utils.flet_translations import translate
from utils.functions import FileSingleton
from views.settings.general._general import GeneralSettings


class InterfaceSettings(ft.Tab):
    def __init__(self, page, instance, **kwargs):
        super().__init__(**kwargs)
        self.text = translate("General Settings")
        self.FileSingleton = FileSingleton()
        data = self.FileSingleton.get_data()

        if "interface" not in data:
            data["interface"] = {"auto_scroll": True, "auto_refresh": True}
            self.FileSingleton.write_data(data)

        self.content = GeneralSettings(page, self, instance)
        # self.content = InterfaceSettings(page, instance)

    def reverse_keyword(self, keyword: str):
        if keyword == "auto_scroll" or keyword == "limit_logs":
            data = self.FileSingleton.get_data()
            data["interface"][keyword] = not data["interface"].get(keyword, False)
            self.FileSingleton.write_data(data)
            if keyword == "auto_scroll":
                for frame in self.page.frames:
                    self.page.frames[frame].logger.auto_scroll = data["interface"][
                        keyword
                    ]
                self.update()
        if keyword == "enabled":
            data = self.FileSingleton.get_data()
            data["discord"]["enabled"] = not data["discord"].get(keyword, False)
            self.FileSingleton.write_data(data)

    def submit(self, e):
        data = self.FileSingleton.get_data()
        data["discord"]["user_id"] = e.control.value
        self.FileSingleton.write_data(data)
