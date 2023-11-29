import flet as ft

from utils.Components.card import GenerateCard
from utils.flet_translations import translate
from views.settings.page_base import BasePage


class PageUpgradeCity(BasePage):
    def __init__(self, profile):
        super().__init__(profile)

        self.add_control(
            GenerateCard(
                level=translate("warning"),
                title=translate("*REQUIREMENT*"),
                subtitle=translate(
                    "If you use the normal way to upgrade the city, you have to configure the city hall position!",
                ),
            ),
            ft.Switch(
                label=translate(
                    "Use normal way to upgrade the city \n(if unchecked the bot is unable to upgrade the pass but \nit is a safer way to upgrade the city)"
                ),
                on_change=self.submit_upgrade_mode,
                value=self.data[str(self.instance_index)]["schedules"][
                    str(self.profile_index)
                ]["upgrade_city_method"]
                == "normal",
                width=300,
            ),
        )

        self.add_control(
            ft.OutlinedButton(
                icon=ft.icons.GPS_FIXED_SHARP,
                text=translate("Set City Hall Position"),
                on_click=lambda _: self.initial_page.go(
                    f"/city-layout/{self.instance_index}/{self.profile_index}"
                ),
            )
        )

    def submit_upgrade_mode(self, e):
        self.data = self.FileSingleton.get_data()
        self.data[str(self.instance_index)]["schedules"][str(self.profile_index)][
            "upgrade_city_method"
        ] = ("normal" if e.control.value else "safest")
        self.FileSingleton.write_data(self.data)
