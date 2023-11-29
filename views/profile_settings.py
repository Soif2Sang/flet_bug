import flet as ft
import flet_route

from views.frametime import ManagerTimezone


def viewProfileSettings(
    page: ft.Page, params: flet_route.Params, basket: flet_route.Basket
) -> ft.View:
    def returnHome():
        page.go("/")

    return ft.View(
        f"/profile/{params.instance_index}/{params.profile_index}/settings",
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
            ManagerTimezone(params.instance_index, params.profile_index),
        ],
    )
