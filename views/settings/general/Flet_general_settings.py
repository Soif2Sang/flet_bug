import flet as ft
from flet_core import ButtonStyle, RoundedRectangleBorder

from utils.flet_translations import translate
from utils.functions import FileSingleton
from views.settings.general.page_profiles import PageProfiles
from views.settings.general.page_redo import PageRedo

color_bank = {"1": "#3b8ed0", "2": "#ba4543", "3": "#dec433"}


class InterfaceSettings(ft.Tab):
    def __init__(self, page, instance, **kwargs):
        super().__init__(**kwargs)
        self.FileSingleton = FileSingleton()
        data = self.FileSingleton.get_data()
        self.initial_page = page
        self.instance_index = instance
        self.profile_index = "1"
        if "interface" not in data:
            data["interface"] = {"auto_scroll": True, "auto_refresh": True}
            self.FileSingleton.write_data(data)

        if "discord" not in data:
            data["discord"] = {"user_id": 0, "enabled": False}
            self.FileSingleton.write_data(data)

        self.text = translate("General Settings")
        self.content: ft.ListView = ft.ListView(
            height=400, expand=1, padding=1, spacing=6
        )

        self.theme = ft.Theme(
            color_scheme=ft.ColorScheme(primary=color_bank[self.profile_index])
        )
        self.init()

    def goBack(self):
        self.content.controls = []
        self.init()
        self.initial_page.update()

    def init(self):
        self.content.controls.extend(
            [
                ft.Container(
                    content=ft.Text(
                        spans=[
                            ft.TextSpan(
                                translate("Shared Profile Preferences"),
                                style=ft.TextStyle(size=15, weight=ft.FontWeight.BOLD),
                            ),
                        ]
                    ),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    padding=ft.padding.all(10),
                    margin=ft.margin.only(top=5, bottom=3),
                ),
            ]
        )
        self.create_advanced_switch("loop_task", "Do tasks again", PageRedo)
        self.create_advanced_switch("scheduler", "run Multiple Profile", PageProfiles)
        self.content.controls.extend(
            [
                ft.TextField(
                    label=translate("Custom API key:"),
                    value=self.data[str(self.instance_index)]["API_KEY"],
                    on_change=lambda e: self.submit(e, "API_KEY", str),
                ),
                ft.Container(
                    content=ft.Text(
                        spans=[
                            ft.TextSpan(
                                text=translate("Interface & Discord Settings"),
                                style=ft.TextStyle(size=15, weight=ft.FontWeight.BOLD),
                            ),
                        ]
                    ),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    padding=ft.padding.all(10),
                    margin=ft.margin.only(top=5, bottom=3),
                ),
                ft.Switch(
                    label=translate("Logger autoscroll"),
                    value=self.data["interface"]["auto_scroll"],
                    on_change=lambda _: self.reverse_keyword("auto_scroll"),
                ),
                ft.Switch(
                    label=translate("Limit Logs to 300 (reduce lags)"),
                    value=self.data["interface"].get("limit_logs", False),
                    on_change=lambda _: self.reverse_keyword("limit_logs"),
                ),
                ft.Switch(
                    label=translate("Enable Discord Notifications"),
                    value=self.data["discord"]["enabled"],
                    on_change=lambda _: self.reverse_keyword("enabled"),
                ),
                ft.TextField(
                    label=translate("Your discord ID"),
                    value=self.data["discord"]["user_id"],
                    on_change=lambda e: self.submit(e, "user_id", int),
                ),
            ]
        )

    def submit(self, e, keyword, method):
        self.data = self.FileSingleton.get_data()
        if keyword == "API_KEY":
            self.data[str(self.instance_index)][keyword] = method(e.control.value)
        if keyword == "user_id":
            self.data["discord"]["user_id"] = method(e.control.value)

        self.FileSingleton.write_data(self.data)

    def reverse_keyword(self, keyword: str, index=None):
        self.data = self.FileSingleton.get_data()

        if keyword in ["auto_scroll", "auto_refresh", "limit_logs"]:
            self.data["interface"][keyword] = not self.data["interface"][keyword]
        elif keyword == "enabled":
            self.data["discord"]["enabled"] = not self.data["discord"].get(
                keyword, False
            )
        elif keyword not in ["loop_task", "scheduler", "leave_game_loop"]:
            self.data[str(self.instance_index)][keyword] = not self.data[
                str(self.instance_index)
            ][keyword]
        else:
            self.data[str(self.instance_index)][keyword] = not self.data[
                str(self.instance_index)
            ][keyword]
        self.FileSingleton.write_data(self.data)

    def create_advanced_switch(self, keyword: str, text: str, function):
        self.data = self.FileSingleton.get_data()
        if keyword not in ["loop_task", "scheduler"]:
            self.content.controls.append(
                ft.Row(
                    controls=[
                        ft.Switch(
                            label=translate(text),
                            value=True
                            if self.data[str(self.instance_index)][keyword]
                            else False,
                            on_change=lambda _: self.reverse_keyword(keyword),
                        ),
                        ft.OutlinedButton(
                            text=translate("Settings"),
                            icon=ft.icons.SETTINGS,
                            on_click=lambda _: function(self),
                            style=ButtonStyle(
                                shape={
                                    ft.MaterialState.DEFAULT: RoundedRectangleBorder(
                                        radius=5
                                    ),
                                }
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                )
            )
        else:
            self.content.controls.append(
                ft.Row(
                    controls=[
                        ft.Switch(
                            label=translate(text),
                            value=True
                            if self.data[str(self.instance_index)][keyword]
                            else False,
                            on_change=lambda _: self.reverse_keyword(keyword),
                        ),
                        ft.OutlinedButton(
                            text=translate("Settings"),
                            icon=ft.icons.SETTINGS,
                            on_click=lambda _: function(self),
                            style=ButtonStyle(
                                shape={
                                    ft.MaterialState.DEFAULT: RoundedRectangleBorder(
                                        radius=5
                                    ),
                                },
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            )
