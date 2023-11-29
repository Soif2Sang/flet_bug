# coding=UTF-8
import json
import os
import subprocess
import sys
import traceback
from time import sleep

import flet as ft
from flet_route import Routing, path

import views.tiles.tile
from utils.auth import selfApi
from utils.Components.AnimatedCard import AnimatedCard
from utils.Components.filescan import generate_filescan
from utils.Components.maintenance import generate_maintenance
from utils.constants import BREZILIAN, toasts_history
from utils.functions import FileSingleton, getchecksum
from views.login.login import LoginUI

from utils.flet_toast.core import Position
from utils.flet_toast.toasts_flexible import ToastsFlexible
from utils.singletons import ApiSingleton, EmulatorSingleton, LinkSingleton
from views.city_layout import viewCityLayout
from views.config_path import find_file_in_all_drives
from views.main import Main
from views.profile_settings import viewProfileSettings

try:
    1
except Exception as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback_list = traceback.format_exception(exc_type, exc_value, exc_traceback)
    traceback_str = "".join(traceback_list)

    def handleError(page: ft.Page):
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.add(
            ft.Text("An error occurred, a log message have been sent to the developer")
        )
        page.add(ft.Text(value=traceback_str, color="red"))
        page.update()

    keyauthapp = selfApi(
        name="Rokbd" if not BREZILIAN else "RokbdBR",
        ownerid="7oofxdj8uH",
        secret="a968396e3fdfff2a2eaf14516fb283b7b7013e19cf392c863c90e0d8c41d9be0"
        if not BREZILIAN
        else "6d15b7ee5e7312238105efd4b648535835dc1ce5f4250fe2dc82910db43147b6",
        version="2.0",
        hash_to_check=getchecksum(),
    )

    keyauthapp.log(traceback_str)

    ft.app(target=handleError)
    exit()

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
