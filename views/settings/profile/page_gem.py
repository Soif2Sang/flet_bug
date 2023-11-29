import flet as ft

from utils.Components.card import GenerateCard
from utils.flet_translations import translate
from views.settings.page_base import BasePage


class PageGem(BasePage):
    def __init__(self, profile):
        super().__init__(profile)
        self.troop_scan_row = ft.Container(
            ft.Row(
                controls=[
                    ft.Text(
                        value=translate("Available troop scan\nfrequency (seconds)")
                    ),
                    ft.TextField(
                        label=translate("Minimum"),
                        value=self.data[str(self.instance_index)]["schedules"][
                            str(self.profile_index)
                        ]["gem_check1"],
                        width=80,
                        content_padding=ft.padding.all(10),
                        on_change=lambda e: self.submit(e, "gem_check1", int),
                        disabled=self.data[str(self.instance_index)]["schedules"][
                            str(self.profile_index)
                        ]["gather_gem_swipe_check"],
                        input_filter=ft.NumbersOnlyInputFilter(),
                    ),
                    ft.Text("~"),
                    ft.TextField(
                        label=translate("Maximum"),
                        value=self.data[str(self.instance_index)]["schedules"][
                            str(self.profile_index)
                        ]["gem_check2"],
                        width=90,
                        content_padding=ft.padding.all(10),
                        on_change=lambda e: self.submit(e, "gem_check2", int),
                        disabled=self.data[str(self.instance_index)]["schedules"][
                            str(self.profile_index)
                        ]["gather_gem_swipe_check"],
                        input_filter=ft.NumbersOnlyInputFilter(),
                    ),
                ]
            ),
            margin=ft.margin.only(left=50),
        )

        self.area_location = ft.Container(
            content=ft.ResponsiveRow(
                controls=[
                    ft.Column(
                        controls=[
                            ft.TextField(
                                label=translate("Your kingdom :"),
                                value=self.data[str(self.instance_index)]["schedules"][
                                    str(self.profile_index)
                                ]["kingdom"],
                                content_padding=ft.padding.all(10),
                                on_change=lambda e: self.submit(e, "kingdom", str),
                                disabled=self.data[str(self.instance_index)][
                                    "schedules"
                                ][str(self.profile_index)]["gather_gem_spiral_method"],
                            )
                        ],
                        col=4,
                    ),
                    ft.Column(
                        controls=[
                            ft.TextField(
                                label=translate("Area location X coordinates :"),
                                value=self.data[str(self.instance_index)]["schedules"][
                                    str(self.profile_index)
                                ]["city_x"],
                                content_padding=ft.padding.all(10),
                                on_change=lambda e: self.submit(e, "city_x", int),
                                disabled=self.data[str(self.instance_index)][
                                    "schedules"
                                ][str(self.profile_index)]["gather_gem_spiral_method"],
                            )
                        ],
                        col=4,
                    ),
                    ft.Column(
                        controls=[
                            ft.TextField(
                                label=translate("Area location Y coordinates :"),
                                value=self.data[str(self.instance_index)]["schedules"][
                                    str(self.profile_index)
                                ]["city_y"],
                                content_padding=ft.padding.all(10),
                                on_change=lambda e: self.submit(e, "city_y", int),
                                disabled=self.data[str(self.instance_index)][
                                    "schedules"
                                ][str(self.profile_index)]["gather_gem_spiral_method"],
                            )
                        ],
                        col=4,
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            margin=ft.margin.only(left=50),
        )

        self.number_of_nodes = ft.Container(
            content=ft.ResponsiveRow(
                controls=[
                    ft.Column(
                        controls=[
                            ft.TextField(
                                label=translate("Fixed number of nodes to gather :"),
                                value=self.data[str(self.instance_index)]["schedules"][
                                    str(self.profile_index)
                                ]["gather_gem_note_limit"],
                                content_padding=ft.padding.all(10),
                                on_change=lambda e: self.submit(
                                    e, "gather_gem_note_limit", int
                                ),
                                disabled=not self.data[str(self.instance_index)][
                                    "schedules"
                                ][str(self.profile_index)][
                                    "gather_gem_enable_node_limit"
                                ],
                                input_filter=ft.NumbersOnlyInputFilter(),
                            )
                        ],
                        col=12,
                    )
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            margin=ft.margin.only(left=50),
        )

        self.add_control(
            GenerateCard(
                level=translate("warning"),
                title=translate("*REQUIREMENT*"),
                subtitle=translate(
                    "Pre-configure yellow-lineups with gathering gem commanders!"
                ),
                margin=ft.margin.only(bottom=20),
            ),
            ft.ResponsiveRow(
                controls=[
                    ft.Column(
                        controls=[
                            ft.TextField(
                                label=translate("Minimum running duration (mins)"),
                                value=self.data[str(self.instance_index)]["schedules"][
                                    str(self.profile_index)
                                ]["gather_gem_duration1"],
                                content_padding=ft.padding.all(10),
                                on_change=lambda e: self.submit(
                                    e, "gather_gem_duration1", int
                                ),
                                input_filter=ft.NumbersOnlyInputFilter(),
                            )
                        ],
                        col=4,
                    ),
                    ft.Column(
                        controls=[
                            ft.TextField(
                                label=translate("Maximum running duration (mins)"),
                                value=self.data[str(self.instance_index)]["schedules"][
                                    str(self.profile_index)
                                ]["gather_gem_duration2"],
                                content_padding=ft.padding.all(10),
                                on_change=lambda e: self.submit(
                                    e, "gather_gem_duration2", int
                                ),
                                input_filter=ft.NumbersOnlyInputFilter(),
                            )
                        ],
                        col=4,
                    ),
                    ft.Column(
                        controls=[
                            ft.TextField(
                                label=translate("Scanning radius (km) :"),
                                value=self.data[str(self.instance_index)]["schedules"][
                                    str(self.profile_index)
                                ]["radius"],
                                width=300,
                                content_padding=ft.padding.all(10),
                                on_change=lambda e: self.submit(e, "radius", int),
                                input_filter=ft.NumbersOnlyInputFilter(),
                            )
                        ],
                        col=4,
                    ),
                ]
            ),
            ft.Switch(
                label=translate("Spiral path method (only around your city)"),
                value=True
                if self.data[str(self.instance_index)]["schedules"][
                    str(self.profile_index)
                ]["gather_gem_spiral_method"]
                else False,
                on_change=lambda _: self.reverse_keyword("gather_gem_spiral_method"),
            ),
            self.area_location,
            ft.Switch(
                label=translate("Detect free marches without clicking on the node"),
                value=True
                if self.data[str(self.instance_index)]["schedules"][
                    str(self.profile_index)
                ]["gather_gem_swipe_check"]
                else False,
                on_change=lambda _: self.reverse_keyword("gather_gem_swipe_check"),
            ),
            self.troop_scan_row,
            ft.Switch(
                label=translate("Set the maximum of nodes to gather"),
                value=True
                if self.data[str(self.instance_index)]["schedules"][
                    str(self.profile_index)
                ]["gather_gem_enable_node_limit"]
                else False,
                on_change=lambda _: self.reverse_keyword(
                    "gather_gem_enable_node_limit"
                ),
            ),
            self.number_of_nodes,
            ft.Switch(
                label=translate(
                    "Recenter the view based on city location\n(turn off if the cords are NOT your city's cords)"
                ),
                value=True
                if self.data[str(self.instance_index)]["schedules"][
                    str(self.profile_index)
                ]["recenter_feature"]
                else False,
                on_change=lambda _: self.reverse_keyword("recenter_feature"),
            ),
            ft.Switch(
                label=translate(
                    "Compare march speed (Increase gem gathering\nbut increase number of actions"
                ),
                value=True
                if self.data[str(self.instance_index)]["schedules"][
                    str(self.profile_index)
                ]["gather_gem_compare_march_duration"]
                else False,
                on_change=lambda _: self.reverse_keyword(
                    "gather_gem_compare_march_duration"
                ),
            ),
            ft.Switch(
                label=translate("Restart the game randomly"),
                value=True
                if self.data[str(self.instance_index)]["schedules"][
                    str(self.profile_index)
                ]["restart_game"]
                else False,
                on_change=lambda _: self.reverse_keyword("restart_game"),
            ),
            # ft.Switch(
            #     label=translate("Experimental feature"),
            #
            #     value=True if self.data[str(self.instance_index)]['schedules'][str(self.profile_index)][
            #         "gem_experimental"] else False,
            #     on_change=lambda _: self.reverse_keyword("gem_experimental")
            # ),
        )

    def reverse_keyword(self, keyword: str):
        super().reverse_keyword(keyword)
        self.data = self.FileSingleton.get_data()

        if keyword == "gather_gem_swipe_check":
            is_disabled = self.data[str(self.instance_index)]["schedules"][
                str(self.profile_index)
            ][keyword]
            self.troop_scan_row.content.controls[1].disabled = is_disabled
            self.troop_scan_row.content.controls[3].disabled = is_disabled
        if keyword == "gather_gem_spiral_method":
            is_disabled = self.data[str(self.instance_index)]["schedules"][
                str(self.profile_index)
            ][keyword]
            self.area_location.content.controls[0].controls[0].disabled = is_disabled
            self.area_location.content.controls[1].controls[0].disabled = is_disabled
            self.area_location.content.controls[2].controls[0].disabled = is_disabled
        if keyword == "gather_gem_enable_node_limit":
            is_disabled = not self.data[str(self.instance_index)]["schedules"][
                str(self.profile_index)
            ][keyword]
            self.number_of_nodes.content.controls[0].controls[0].disabled = is_disabled

        self.profile.initial_page.update()
