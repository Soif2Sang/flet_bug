import flet as ft

from utils.Components.card import GenerateCard
from utils.flet_translations import translate
from views.settings.page_base import BasePage
from views.settings.profile.cols.Flet_col_transfer import FletColumnRss


class PageTransfer(BasePage):
    def __init__(self, profile):
        super().__init__(profile)

        self.add_control(
            GenerateCard(
                level=translate("warning"),
                subtitle=translate(
                    "In order to use this feature, you have to purchase a API key on 2captcha.com (this is very cheap!)"
                ),
            ),
            self.create_normal_switch(
                "fast_rss_transfer", "Enable faster rss transfer may be riskier"
            ),
            FletColumnRss(self.instance_index, self.profile_index),
            ft.Divider(),
            ft.OutlinedButton(
                icon=ft.icons.GPS_FIXED_SHARP,
                text=translate("Set City Position"),
                on_click=lambda _: self.initial_page.go(
                    f"/city-layout/{self.instance_index}/{self.profile_index}"
                ),
            ),
        )
