import flet as ft


def generate_filescan():
    return ft.Card(
        content=ft.Container(
            content=ft.ListTile(
                title=ft.Text(
                    "The Bot is scanning the drives for emulator configuration, please wait a bit.."
                ),
                leading=ft.Icon(ft.icons.FIND_IN_PAGE_OUTLINED),
            ),
            width=400,
            padding=10,
        ),
        color=ft.colors.SURFACE_VARIANT,
    )
