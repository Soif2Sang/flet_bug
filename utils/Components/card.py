import flet as ft


def GenerateCard(level=None, title=None, subtitle=None, margin=None, height=None):
    if level == "warning":
        leading = ft.Icon(ft.icons.WARNING, color=ft.colors.RED)
    elif level == "tips":
        leading = ft.Icon(ft.icons.TIPS_AND_UPDATES, color=ft.colors.AMBER_500)
    else:
        leading = ft.Icon(ft.icons.INFO_OUTLINED)

    if title:
        title = ft.Text(title, size=14, weight=ft.FontWeight.BOLD)

    if subtitle:
        subtitle = ft.Text(value=subtitle, size=12, weight=ft.FontWeight.W_700)

    return ft.Card(
        content=ft.Container(
            content=ft.Column(
                [ft.ListTile(leading=leading, title=title, subtitle=subtitle)]
            ),
            width=400,
            padding=10,
            height=height,
        ),
        margin=margin,
        color=ft.colors.SURFACE_VARIANT,
    )
