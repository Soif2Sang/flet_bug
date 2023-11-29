import flet as ft
from tiles.handler.config_handler import FrameUpgrade
from tiles.tile import ConfigOverrider

from utils.functions import FileSingleton


class TileUpgrade(ft.Row):
    def __init__(self, page, number, **kwargs):
        super().__init__(**kwargs)

        self.tile_manager = None
        data = FileSingleton().get_data()

        self.selected = False
        self.page = page
        self.initial_page = page

        self.number = number

        self.started = False
        self.stopped = False
        self.tasks_process = None

        self.button_select = ft.IconButton(
            icon=ft.icons.PAGEVIEW,
            selected_icon=ft.icons.REMOVE_RED_EYE_OUTLINED,
            on_click=lambda _: self.select(),
        )

        self.enable_switch = ft.Switch(on_change=lambda _: self.change(), value=False)
        self.text_name = ft.Text(value=data[str(number)]["name"], width=150)

        self.config_overrider = ConfigOverrider(self.initial_page, number)

        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN
        self.controls.extend(
            [
                ft.Row(
                    controls=[
                        self.button_select,
                        self.enable_switch,
                        self.text_name,
                    ]
                ),
                self.config_overrider,
            ]
        )

    def change(self):
        self.selected = not self.selected

    def select(self):
        self.page.tile_manager.unselect_all()
        self.button_select.selected = True
        # print(f"{len(self.page.controls)>2 =}")
        if len(self.page.controls) > 2:
            self.page.controls.pop()
        if self.number not in self.page.frames:
            self.page.frames[self.number] = FrameUpgrade(self.page, self.number)
        self.page.add(self.page.frames[self.number])
        # self.page.title = f"{time()}"
        self.update()

    def get_enabled_sel(self):
        return self.tile_manager.get_enabled_sel()
