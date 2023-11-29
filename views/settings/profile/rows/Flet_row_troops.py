import flet as ft

from utils.flet_translations import translate
from utils.functions import FileSingleton


class FletRowTraining(ft.ResponsiveRow):
    def __init__(self, key, instance_index, profile_index):
        super().__init__()
        self.FileSingleton = FileSingleton()
        self.data = self.FileSingleton.get_data()
        self.instance_index = instance_index
        self.profile_index = profile_index
        self.content_padding = ft.padding.all(10)
        self.controls = [
            ft.Switch(
                label=translate(f"Train {key}"),
                value=self.data[str(self.instance_index)]["schedules"][
                    str(self.profile_index)
                ][f"{key}_enable"],
                on_change=lambda e: self.submit(e, f"{key}_enable", bool),
                col=6,
            ),
            ft.Dropdown(
                width=140,
                label="Tier",
                options=[
                    ft.dropdown.Option("t1"),
                    ft.dropdown.Option("t2"),
                    ft.dropdown.Option("t3"),
                    ft.dropdown.Option("t4"),
                    ft.dropdown.Option("t5"),
                ],
                value=self.data[str(self.instance_index)]["schedules"][
                    str(self.profile_index)
                ][f"{key}_tier"],
                on_change=lambda e: self.submit(e, f"{key}_tier", str),
                height=40,
                content_padding=ft.Padding(
                    left=5, top=3, right=5, bottom=3
                ),  # modify to your likings
                col=6,
            ),
        ]

    def submit(self, e, keyword, method):
        self.data = self.FileSingleton.get_data()

        if keyword in ["time_to_wait_loop2", "time_to_wait_loop1", "API_KEY"]:
            self.data[str(self.instance_index)][keyword] = method(e.control.value)
            print(self.data[str(self.instance_index)][keyword])
            self.FileSingleton.write_data(self.data)
            return
        if keyword not in ["sleep_multiplicator", "defeat_barbarians"]:
            self.data[str(self.instance_index)]["schedules"][str(self.profile_index)][
                keyword
            ] = method(e.control.value)
        else:
            self.data[str(self.instance_index)]["schedules"][str(self.profile_index)][
                keyword
            ] = float(e.control.value.replace("x", "").replace("level ", ""))
        self.FileSingleton.write_data(self.data)
