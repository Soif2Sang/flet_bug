import flet as ft

from utils.flet_translations import translate
from views.settings.page_base import BasePage


class PageHeal(BasePage):
    def __init__(self, profile):
        super().__init__(profile)

        self.add_control(
            ft.TextField(
                label=translate("Heal batch :"),
                value=self.data[str(self.instance_index)]["schedules"][
                    str(self.profile_index)
                ]["healing_count"],
                width=300,
                on_change=lambda e: self.submit(e, "healing_count", int),
                content_padding=ft.padding.all(10),
            ),
            ft.Divider(),
            ft.OutlinedButton(
                icon=ft.icons.GPS_FIXED_SHARP,
                text=translate("Set Hospital position"),
                on_click=lambda _: self.initial_page.go(
                    f"/city-layout/{self.instance_index}/{self.profile_index}"
                ),
            ),
        )
