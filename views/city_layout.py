import base64
import traceback

import flet as ft
import flet_route

from utils.functions import FileSingleton


class cityLayoutParam(flet_route.Params):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance_index = None
        self.profile_index = None


def image_to_base64(image_byte):
    encoded_string = base64.b64encode(image_byte.read())
    return encoded_string.decode("utf-8")


def viewCityLayout(
    page: ft.Page, params: cityLayoutParam, basket: flet_route.Basket
) -> ft.View:
    page.window_width = 900
    page.window_height = 500
    image_byte = image_to_base64(
        page.tile_manager.tiles[
            str(params.instance_index)
        ].runner.adb.get_curr_device_screen_img_bytesIO()
    )

    def returnHome():
        page.window_width = 450
        page.window_height = 700
        page.go("/")

    return ft.View(
        f"/city-layout/{params.instance_index}/{params.profile_index}",
        controls=[
            ft.Container(
                bgcolor=ft.colors.SURFACE_VARIANT,
                content=ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.ARROW_BACK, on_click=lambda _: returnHome()
                        ),
                        ft.Text(value="Go back"),
                    ]
                ),
            ),
            ft.Text(
                value="Click on the building button you wanna set, then click in the center of the building."
            ),
            CityPlacement(image_byte, params.instance_index, params.profile_index),
        ],
    )


class CityPlacement(ft.Container):
    button = {
        "infantry_camp": "Inf",
        "cavalry_camp": "Cav",
        "archery_camp": "Arch",
        "siege_camp": "Siege",
        "hospital": "Hosp",
        "scout_camp": "Scout",
        "city_transfer": "Transfer",
        "city_hall_position": "CH",
        "academy_position": "Academy",
    }

    def __init__(self, image64, instance, profile, **kwargs):
        super().__init__(**kwargs)
        self.instance = instance
        self.profile = profile
        self.current_build = None
        self.FileSingleton = FileSingleton()
        self.data = self.FileSingleton.get_data()

        self.main_container = ft.Stack(
            controls=[
                ft.Container(
                    image_src_base64=image64,
                    height=720 / 2,
                    width=1280 / 2,
                    on_click=self.on_tap_update,
                )
            ]
        )

        self.buttons = ft.ListView(height=720 / 2, expand=True, spacing=1)
        self.content = ft.Row(controls=[self.main_container, self.buttons])

        for key, item in self.button.items():
            button_text = f"Set {key.replace('_', ' ').title()}"
            button_click_handler = lambda _, name=key: self.setCurrentBuild(name)
            button = ft.ElevatedButton(text=button_text, on_click=button_click_handler)
            self.buttons.controls.append(button)

            value = self.data[str(self.instance)]["schedules"][str(self.profile)][key]
            if value:
                self.main_container.controls.append(
                    ft.Chip(
                        label=ft.Text(item),
                        on_delete=self.remove_self,
                        delete_icon_tooltip="remove",
                        top=value[1] / 2 - 10,
                        left=value[0] / 2 - 10,
                        label_padding=0,
                        key=key,
                        opacity=0.7,
                    )
                )

    def setCurrentBuild(self, param: str):
        self.current_build = param

        for element in self.buttons.controls:
            element.color = "blue"

        index = -1
        for i, element in enumerate(self.button.keys()):
            if element == param:
                index = i

        self.buttons.controls[index].color = "red"
        self.buttons.page.update()

    def on_tap_update(self, e: ft.TapEvent):
        if self.current_build is None:
            return
        left, top = e.local_x, e.local_y

        try:
            self.data = self.FileSingleton.get_data()
            self.data[str(self.instance)]["schedules"][str(self.profile)][
                self.current_build
            ] = (int(e.local_x * 2), int(e.local_y * 2))

        except Exception:
            traceback.print_exc()
            return

        for element in self.buttons.controls:
            element.color = "blue"

        for element in self.main_container.controls:
            if isinstance(element, ft.Chip):
                if element.label.value == self.button[self.current_build]:
                    self.main_container.controls.remove(element)

        self.FileSingleton.write_data(self.data)
        self.data = self.FileSingleton.get_data()

        self.main_container.controls.append(
            ft.Chip(
                label=ft.Text(self.button[self.current_build]),
                on_delete=self.remove_self,
                delete_icon_tooltip="remove",
                top=top - 10,
                left=left - 10,
                label_padding=0,
                key=self.current_build,
                opacity=0.7,
            )
        )
        self.page.update()

    def remove_self(self, e):
        self.main_container.controls.remove(e.control)
        print(e.control)
        print(e.control.key)
        try:
            self.data = self.FileSingleton.get_data()
            print(
                self.data[str(self.instance)]["schedules"][str(self.profile)][
                    e.control.key
                ]
            )

            self.data[str(self.instance)]["schedules"][str(self.profile)][
                e.control.key
            ] = []

        except Exception:
            traceback.print_exc()
            return
        print(
            self.data[str(self.instance)]["schedules"][str(self.profile)][e.control.key]
        )

        self.FileSingleton.write_data(self.data)
        self.page.update()
