import flet as ft

from utils.Components.card import GenerateCard
from utils.flet_translations import translate
from views.settings.page_base import BasePage
from views.settings.profile.rows.Flet_row_presets import FletRowPresets


class PageMarauders(BasePage):
    def __init__(self, profile):
        super().__init__(profile)

        self.add_control(
            GenerateCard(
                level=translate("tips"),
                margin=ft.margin.only(bottom=20),
                subtitle=translate(
                    "Pre-configure your red lineups with commanders who have the same march speed.\nIf you intend to use this feature extensively, I recommend running it for 3-4 hours and enabling the option to redo tasks. This will allow your troops to return to the city for healing."
                ),
            ),
            ft.Container(
                content=ft.ResponsiveRow(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.TextField(
                                    label=translate("Your kingdom :"),
                                    value=self.data[str(self.instance_index)][
                                        "schedules"
                                    ][str(self.profile_index)]["kingdom"],
                                    content_padding=ft.padding.all(10),
                                    on_change=lambda e: self.submit(e, "kingdom", str),
                                )
                            ],
                            col=4,
                        ),
                        ft.Column(
                            controls=[
                                ft.TextField(
                                    label=translate("Area location X coordinates :"),
                                    value=self.data[str(self.instance_index)][
                                        "schedules"
                                    ][str(self.profile_index)]["city_x"],
                                    content_padding=ft.padding.all(10),
                                    on_change=lambda e: self.submit(e, "city_x", int),
                                    input_filter=ft.NumbersOnlyInputFilter(),
                                )
                            ],
                            col=4,
                        ),
                        ft.Column(
                            controls=[
                                ft.TextField(
                                    label=translate("Area location Y coordinates :"),
                                    value=self.data[str(self.instance_index)][
                                        "schedules"
                                    ][str(self.profile_index)]["city_y"],
                                    content_padding=ft.padding.all(10),
                                    on_change=lambda e: self.submit(e, "city_y", int),
                                    input_filter=ft.NumbersOnlyInputFilter(),
                                )
                            ],
                            col=4,
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                margin=ft.margin.only(bottom=10),
            ),
            ft.ResponsiveRow(
                controls=[
                    ft.Column(
                        controls=[
                            ft.TextField(
                                label=translate("Minimum Killing Duration (mins)"),
                                value=self.data[str(self.instance_index)]["schedules"][
                                    str(self.profile_index)
                                ]["kill_marauders_duration"][0],
                                content_padding=ft.padding.all(10),
                                on_change=lambda e: self.submit_marauders(e, 0),
                                input_filter=ft.NumbersOnlyInputFilter(),
                            )
                        ],
                        col=6,
                    ),
                    ft.Column(
                        controls=[
                            ft.TextField(
                                label=translate("Maximum Killing Duration (mins)"),
                                value=self.data[str(self.instance_index)]["schedules"][
                                    str(self.profile_index)
                                ]["kill_marauders_duration"][1],
                                content_padding=ft.padding.all(10),
                                on_change=lambda e: self.submit_marauders(e, 1),
                                input_filter=ft.NumbersOnlyInputFilter(),
                            )
                        ],
                        col=6,
                    ),
                ]
            ),
            ft.Divider(),
            ft.Text(value=translate("Peacekeeper presets")),
            ft.Column(
                controls=[
                    FletRowPresets(
                        self.instance_index, self.profile_index, str(preset_index)
                    )
                    for preset_index in range(1, 8)
                ],
                wrap=True,
                spacing=10,
                run_spacing=10,
                height=150,
            ),
        )

    def submit_marauders(self, e, index):
        self.data = self.FileSingleton.get_data()
        self.data[str(self.instance_index)]["schedules"][str(self.profile_index)][
            "kill_marauders_duration"
        ][index] = (
            e.control.value
            if e.control.value is not None or e.control.value != ""
            else 0
        )
        self.FileSingleton.write_data(self.data)
