import flet as ft

from utils.Components.card import GenerateCard
from utils.flet_translations import translate
from views.settings.page_base import BasePage


class PageFog(BasePage):
    def __init__(self, profile):
        super().__init__(profile)

        self.add_control(
            # ft.Card(
            #     content=ft.Container(
            #         content=ft.Column(
            #             [
            #                 ft.ListTile(
            #                     leading=ft.Icon(ft.icons.TIPS_AND_UPDATES, color=ft.colors.AMBER_500),
            #                     subtitle=ft.Text(
            #                         value="If you plan on having the safest configuration, do not use this functionality extensively throughout the day.",
            #                         size=12,
            #                         weight=ft.FontWeight.W_700
            #                     ),
            #
            #                 )
            #             ]
            #         ),
            #         width=400,
            #         padding=10,
            #         height=90
            #     ),
            #     # color=ft.colors.INDIGO_300,
            # ),
            GenerateCard(
                level=translate("tips"),
                subtitle=translate(
                    "If you plan on having the safest configuration, do not use this functionality extensively throughout the day."
                ),
            ),
            ft.Row(
                controls=[
                    ft.Text(translate("Scout duration (mins)")),
                    ft.TextField(
                        label=translate("Minimum"),
                        value=self.data[str(self.instance_index)]["schedules"][
                            str(self.profile_index)
                        ]["scout_duration1"],
                        width=80,
                        on_change=lambda e: self.submit(e, "scout_duration1", int),
                        content_padding=ft.padding.all(10),
                    ),
                    ft.Text("~"),
                    ft.TextField(
                        label=translate("Maximum"),
                        value=self.data[str(self.instance_index)]["schedules"][
                            str(self.profile_index)
                        ]["scout_duration2"],
                        width=90,
                        on_change=lambda e: self.submit(e, "scout_duration2", int),
                        content_padding=ft.padding.all(10),
                    ),
                ]
            ),
            ft.Divider(),
            ft.OutlinedButton(
                icon=ft.icons.GPS_FIXED_SHARP,
                text=translate("Set Scout camp position"),
                on_click=lambda _: self.initial_page.go(
                    f"/city-layout/{self.instance_index}/{self.profile_index}"
                ),
            ),
        )
