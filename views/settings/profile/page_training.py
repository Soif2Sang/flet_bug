import flet as ft

from utils.flet_translations import translate
from views.settings.page_base import BasePage
from views.settings.profile.rows.Flet_row_troops import FletRowTraining


class PageTraining(BasePage):
    def __init__(self, profile):
        super().__init__(profile)

        keys = [
            "infantry",
            "cavalry",
            "archery",
            "siege",
        ]

        for key in keys:
            self.add_control(
                FletRowTraining(
                    key=key,
                    instance_index=self.instance_index,
                    profile_index=self.profile_index,
                )
            )

        self.add_control(
            ft.OutlinedButton(
                icon=ft.icons.GPS_FIXED_SHARP,
                text=translate("Set Training camps position"),
                on_click=lambda _: self.initial_page.go(
                    f"/city-layout/{self.instance_index}/{self.profile_index}"
                ),
            )
        )
