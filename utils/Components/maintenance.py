import flet as ft


def generate_maintenance():
    return ft.Card(
        content=ft.Container(
            content=ft.ListTile(
                title=ft.Text(
                    "The Bot seems to be under maintenance, please wait a bit.."
                ),
                leading=ft.Icon(ft.icons.PORTABLE_WIFI_OFF_SHARP),
            ),
            width=400,
            padding=10,
        ),
        color=ft.colors.SURFACE_VARIANT,
    )
