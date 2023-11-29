import flet as ft

from utils.flet_translations import translate
from utils.functions import FileSingleton


class FletColumnRss(ft.Column):
    def __init__(self, instance_index, profile_index):
        super().__init__()
        self.FileSingleton = FileSingleton()
        self.data = self.FileSingleton.get_data()
        self.instance_index = instance_index
        self.profile_index = profile_index
        self.controls = [
            ft.TextField(
                label=translate("Million of Food to transfer :"),
                value=self.data[str(self.instance_index)]["schedules"][
                    str(self.profile_index)
                ]["transfer_food"],
                on_change=lambda e: self.submit(e, f"transfer_food", int),
                content_padding=ft.padding.all(10),
                input_filter=ft.NumbersOnlyInputFilter(),
            ),
            ft.TextField(
                label=translate("Million of Wood to transfer :"),
                value=self.data[str(self.instance_index)]["schedules"][
                    str(self.profile_index)
                ]["transfer_wood"],
                on_change=lambda e: self.submit(e, f"transfer_wood", int),
                content_padding=ft.padding.all(10),
                input_filter=ft.NumbersOnlyInputFilter(),
            ),
            ft.TextField(
                label=translate("Million of Stone to transfer :"),
                value=self.data[str(self.instance_index)]["schedules"][
                    str(self.profile_index)
                ]["transfer_stone"],
                on_change=lambda e: self.submit(e, f"transfer_stone", int),
                content_padding=ft.padding.all(10),
                input_filter=ft.NumbersOnlyInputFilter(),
            ),
            ft.TextField(
                label=translate("Million of Gold to transfer :"),
                value=self.data[str(self.instance_index)]["schedules"][
                    str(self.profile_index)
                ]["transfer_gold"],
                on_change=lambda e: self.submit(e, f"transfer_gold", int),
                content_padding=ft.padding.all(10),
                input_filter=ft.NumbersOnlyInputFilter(),
            ),
        ]

    def submit(self, e, keyword, method):
        self.data = self.FileSingleton.get_data()

        self.data[str(self.instance_index)]["schedules"][str(self.profile_index)][
            keyword
        ] = (method(e.control.value) if e.control.value != "" else 0)
        self.FileSingleton.write_data(self.data)
