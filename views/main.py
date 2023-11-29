import flet as ft

from views.tiles.handler.logging_handler import Logger, LoggerUpgrade
from views.tiles.handler.tile_handler_u import TileManagerUpgrade
from utils.constants import VERSION, toasts_history
from utils.flet_toast.core import Position
from utils.flet_toast.toasts_flexible import ToastAction, ToastsFlexible
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
    if page.UPGRADE:
        page.tile_manager = TileManagerUpgrade(page)
        page.logger = LoggerUpgrade(page)
    else:
        page.tile_manager = TileHandler(page)
    page.body = ft.Column(controls=[page.tile_manager, ft.Divider(height=0)])
    if page.UPGRADE:
        page.body.controls.append(page.tile_manager.start_bar)
        page.body.controls.append(page.logger)

    page.go("/")
    page.tile_manager.refresh()

if __name__ == "__main__":
    ft.app(target=Main, view=ft.FLET_APP)
