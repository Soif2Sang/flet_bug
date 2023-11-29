import flet as ft

from utils.functions import FileSingleton


class FletRowPresets(ft.Row):
    def __init__(self, instance_index, profile_index, preset_index):
        super().__init__()
        self.FileSingleton = FileSingleton()
        self.data = self.FileSingleton.get_data()
        self.instance_index = instance_index
        self.profile_index = profile_index
        self.preset_index = preset_index
        self.content_padding = ft.padding.all(10)
        self.controls = [
            ft.Checkbox(
                label=f"Preset {preset_index}",
                on_change=lambda e: self.submit(e),
                value=self.data[str(self.instance_index)]["schedules"][
                    str(self.profile_index)
                ]["barbarians_preset"][preset_index],
            )
        ]

    def submit(self, e):
        self.data = self.FileSingleton.get_data()
        self.data[str(self.instance_index)]["schedules"][str(self.profile_index)][
            "barbarians_preset"
        ][self.preset_index] = bool(e.control.value)
        self.FileSingleton.write_data(self.data)
