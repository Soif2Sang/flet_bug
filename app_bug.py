# coding=UTF-8

import flet as ft
from flet_route import Routing, path

from views.main import Main


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 450
    page.window_height = 400

    page.body = ft.Column()

    page.app_routes = [
        path(url="/", clear=True, view=index),
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
