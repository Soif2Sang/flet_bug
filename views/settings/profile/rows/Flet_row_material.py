import flet as ft

from utils.flet_translations import translate
from utils.functions import FileSingleton


class FletRowMaterial(ft.Row):
    def __init__(self, keys, i, instance_index, profile_index):
        super().__init__()
        self.FileSingleton = FileSingleton()
        self.data = self.FileSingleton.get_data()
        self.instance_index = instance_index
        self.profile_index = profile_index
        self.controls = [
            ft.Container(
                width=100,
                content=ft.Text(translate(f"{keys[i - 1]} choice :")),
                alignment=ft.alignment.center_right,
            ),
            ft.Dropdown(
                width=140,
                height=50,
                content_padding=ft.Padding(
                    left=5, top=3, right=5, bottom=3
                ),  # modify to your likings
                label="Type",
                options=[
                    ft.dropdown.Option("leather"),
                    ft.dropdown.Option("stone"),
                    ft.dropdown.Option("ebony"),
                    ft.dropdown.Option("bones"),
                ],
                value=self.data[str(self.instance_index)]["schedules"][
                    str(self.profile_index)
                ][f"material_choice_{i}"],
                on_change=lambda e: self.submit(e, f"material_choice_{i}", str),
            ),
        ]

    def submit(self, e, keyword, method):
        self.data = self.FileSingleton.get_data()
        if keyword in ["time_to_wait_loop2", "time_to_wait_loop1", "API_KEY"]:
            self.data[str(self.instance_index)][keyword] = method(e.control.value)
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
