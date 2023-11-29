import flet as ft
from flet_core import ButtonStyle, RoundedRectangleBorder

from utils.flet_translations import translate
from views.settings.page_base import BasePage


class PageProfiles(BasePage):
    def __init__(self, profile):
        super().__init__(profile)

        self.add_control(
            ft.Row(
                controls=[
                    ft.Switch(
                        label=translate("Profile n°1"),
                        active_track_color="#3b8ed0",
                        value=True
                        if self.data[str(self.instance_index)]["schedules"][str(1)][
                            "enabled"
                        ]
                        else False,
                        on_change=lambda _: self.reverse_keyword("enabled", 1),
                    ),
                    ft.OutlinedButton(
                        text=translate("Settings"),
                        icon_color="#3b8ed0",
                        icon=ft.icons.SETTINGS,
                        on_click=lambda _: self.initial_page.go(
                            f"/profile/{self.instance_index}/1/settings"
                        ),
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
            ),
            ft.Row(
                controls=[
                    ft.Switch(
                        label=translate("Profile n°2"),
                        active_track_color="#ba4543",
                        value=True
                        if self.data[str(self.instance_index)]["schedules"][str(2)][
                            "enabled"
                        ]
                        else False,
                        on_change=lambda _: self.reverse_keyword("enabled", 2),
                    ),
                    ft.OutlinedButton(
                        text=translate("Settings"),
                        icon_color="#ba4543",
                        icon=ft.icons.SETTINGS,
                        on_click=lambda _: self.initial_page.go(
                            f"/profile/{self.instance_index}/2/settings"
                        ),
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
            ),
            ft.Row(
                controls=[
                    ft.Switch(
                        label=translate("Profile n°3"),
                        active_track_color="#dec433",
                        value=True
                        if self.data[str(self.instance_index)]["schedules"][str(3)][
                            "enabled"
                        ]
                        else False,
                        on_change=lambda _: self.reverse_keyword("enabled", 3),
                    ),
                    ft.OutlinedButton(
                        text=translate("Settings"),
                        icon_color="#dec433",
                        icon=ft.icons.SETTINGS,
                        on_click=lambda _: self.initial_page.go(
                            f"/profile/{self.instance_index}/3/settings"
                        ),
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
            ),
        )
        self.profile.initial_page.update()

    def reverse_keyword(self, keyword: str, index=None):
        if index is None:
            index = self.profile_index

        self.data = self.FileSingleton.get_data()

        if keyword in ["auto_scroll", "auto_refresh", "limit_logs"]:
            self.data["interface"]["keyword"] = not self.data["interface"]["keyword"]
        elif keyword not in ["loop_task", "scheduler", "leave_game_loop"]:
            self.data[str(self.instance_index)]["schedules"][str(index)][
                keyword
            ] = not self.data[str(self.instance_index)]["schedules"][str(index)][
                keyword
            ]
        else:
            self.data[str(self.instance_index)][keyword] = not self.data[
                str(self.instance_index)
            ][keyword]
        self.FileSingleton.write_data(self.data)
