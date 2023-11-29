import flet as ft

from utils.Components.card import GenerateCard
from utils.flet_translations import translate
from views.settings.page_base import BasePage


class PageRedo(BasePage):
    def __init__(self, profile):
        super().__init__(profile)

        self.add_control(
            GenerateCard(
                level="warning",
                title=translate("Time to wait until the bot do the task again."),
                subtitle=translate(
                    "You need to be aware that using tight timings can lead to unwanted behaviors."
                ),
            ),
            ft.Switch(
                label=translate("Close the game after all the tasks are done"),
                value=self.data[str(self.instance_index)]["leave_game_loop"],
                on_change=lambda _: self.reverse_keyword("leave_game_loop"),
            ),
            ft.Container(
                ft.Text(
                    translate("Minutes to wait until the bot do the task :"),
                ),
                margin=ft.margin.only(left=5),
            ),
            ft.Container(
                content=ft.ResponsiveRow(
                    controls=[
                        ft.TextField(
                            label=translate("Minimum"),
                            value=self.data[str(self.instance_index)][
                                "time_to_wait_loop1"
                            ],
                            on_change=lambda e: self.submit(
                                e, "time_to_wait_loop1", int
                            ),
                            content_padding=ft.padding.all(10),
                            col=4,
                            input_filter=ft.NumbersOnlyInputFilter(),
                        ),
                        ft.TextField(
                            label=translate("Maximum"),
                            value=self.data[str(self.instance_index)][
                                "time_to_wait_loop2"
                            ],
                            on_change=lambda e: self.submit(
                                e, "time_to_wait_loop2", int
                            ),
                            content_padding=ft.padding.all(10),
                            col=4,
                            input_filter=ft.NumbersOnlyInputFilter(),
                        ),
                    ],
                ),
                margin=ft.margin.only(left=50, top=5),
            ),
        )
        self.profile.initial_page.update()
