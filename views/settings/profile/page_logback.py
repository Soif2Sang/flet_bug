import flet as ft

from utils.flet_translations import translate
from views.settings.page_base import BasePage


class PageLogback(BasePage):
    def __init__(self, profile):
        super().__init__(profile)

        self.add_control(
            ft.Text(
                spans=[
                    ft.TextSpan(
                        text=translate(
                            "Time to wait before the bot log  back from your connection(minutes):"
                        ),
                        style=ft.TextStyle(size=15),
                    )
                ]
            ),
            ft.Row(
                controls=[
                    ft.TextField(
                        label=translate("Minimum"),
                        value=self.data[str(self.instance_index)]["schedules"][
                            str(self.profile_index)
                        ]["log_back1"],
                        width=80,
                        on_change=lambda e: self.submit(e, "log_back1", int),
                        input_filter=ft.NumbersOnlyInputFilter(),
                    ),
                    ft.Text("~"),
                    ft.TextField(
                        label=translate("Maximum"),
                        value=self.data[str(self.instance_index)]["schedules"][
                            str(self.profile_index)
                        ]["log_back2"],
                        width=90,
                        on_change=lambda e: self.submit(e, "log_back2", int),
                        input_filter=ft.NumbersOnlyInputFilter(),
                    ),
                ]
            ),
        )
