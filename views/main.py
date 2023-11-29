import flet as ft

from views.tiles.handler.tile_handler import TileHandler

color_bank = {1: "#3b8ed0", 2: "#ba4543", 3: "#dec433"}


def Main(page: ft.Page, days=950):
    # page.clean()
    theme = ft.Theme()
    theme.page_transitions.windows = ft.PageTransitionTheme.CUPERTINO
    page.vertical_alignment = None
    page.horizontal_alignment = None
    page.frames = {}
    page.window_resizable = True
    page.window_width = 450
    page.window_height = 700
    page.theme = theme
    page.tile_manager = TileHandler(page)
    page.body = ft.Column(controls=[page.tile_manager, ft.Divider(height=0)])

    page.go("/")
    page.tile_manager.refresh()

if __name__ == "__main__":
    ft.app(target=Main, view=ft.FLET_APP)
