# coding=UTF-8

import flet as ft
from flet_route import Routing, path

from utils.constants import toasts_history
from utils.flet_toast.core import Position
from utils.flet_toast.toasts_flexible import ToastsFlexible
from utils.functions import FileSingleton
from views.city_layout import viewCityLayout
from views.login.login import LoginUI
from views.main import Main
from views.profile_settings import viewProfileSettings

fileSingleton = FileSingleton()


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 450
    page.window_height = 400
    page.FileSingleton = FileSingleton()

    def create_banner(text):
        return ft.Banner(
            bgcolor=ft.colors.AMBER_100,
            leading=ft.Icon(
                ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40
            ),
            content=ft.Text(value=text),
            actions=[
                ft.TextButton("Ok", on_click=lambda _: page.close_banner()),
            ],
            open=True,
        )

    page.open_banner = lambda text: page.show_banner(create_banner(text))
    page.loginUI = LoginUI(page)
    page.UPGRADE = False
    page.body = ft.Column()

    def generate_toast(title, description, icon=ft.icons.INFO, bgcolor_title="AMBER"):
        ToastsFlexible(
            page=page,
            icon=icon,
            title=title,
            desc=description,
            auto_close=None,
            trigger=None,
            width=360,
            set_history=toasts_history,
            position=Position.TOP_RIGHT,
            bgcolor_title=bgcolor_title,
        )

    page.generate_toast = lambda title, description, icon=ft.icons.INFO, bgcolor_title="AMBER": generate_toast(
        title, description, icon, bgcolor_title
    )

    page.app_routes = [
        path(url="/", clear=True, view=index),
        path(
            url=f"/city-layout/:instance_index/:profile_index",
            clear=True,
            view=viewCityLayout,
        ),
        path(
            url=f"/profile/:instance_index/:profile_index/settings",
            clear=True,
            view=viewProfileSettings,
        ),
    ]

    page.routing = Routing(
        page=page,
        app_routes=page.app_routes,
    )

    page.title = "90 Days left"
    Main(page, 60)

def index(page: ft.Page, params, basket):
    return ft.View(route="/", controls=page.body.controls)

if __name__ == "__main__":
    ft.app(target=main)
