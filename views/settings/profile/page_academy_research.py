import flet as ft

from utils.flet_translations import translate
from views.settings.page_base import BasePage
from views.settings.profile.rows.Flet_row_troops import FletRowTraining


class PageAcademyResearch(BasePage):
    def __init__(self, profile):
        super().__init__(profile)

        self.add_control(
            ft.OutlinedButton(
                icon=ft.icons.GPS_FIXED_SHARP,
                text=translate("Set Academy Research"),
                on_click=lambda _: self.initial_page.go(
                    f"/city-layout/{self.instance_index}/{self.profile_index}"
                ),
            )
        )
