import json
import os
import subprocess

import flet as ft

from utils.functions import FileSingleton
from utils.singletons import EmulatorSingleton
from views.config_path import find_file_in_all_drives
from views.main import Main


def is_str_valid(username, password):
    for element in ["#", "$", "&", "|", "\0", "\n", "\r", "'", "'", '"', "\Z"]:
        if element in username or element in password:
            return False
    return True


class EmulatorChoice(ft.ResponsiveRow):
    def __init__(self, page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial_page = page
        self.fileSingleton = FileSingleton()
        self.data = self.fileSingleton.get_data()
        self.init()

    def go_main(self, e):
        path_file = self.initial_page.FileSingleton.get_path()

        if e.control.data == "bluestacks":
            EmulatorSingleton().setEmulator("bluestacks")

            if not os.path.exists(path_file["bluestacks"]) or not os.path.exists(
                path_file["HD-Player"]
            ):
                self.initial_page.go("/emulator-loading")
                self.initial_page.update()

                if result := find_file_in_all_drives("bluestacks\.conf"):
                    path_file["bluestacks\.conf".split("\\")[0]] = result
                    with open("./path.json", "w", encoding="UTF-8") as f:
                        json.dump(path_file, f, indent=2)

                if result := find_file_in_all_drives("HD-Player\.exe"):
                    path_file["HD-Player\.exe".split("\\")[0]] = result
                    with open("./path.json", "w", encoding="UTF-8") as f:
                        json.dump(path_file, f, indent=2)

            cmd = f"{path_file['HD-Player'].replace('Player', 'Adb')} start-server"
            subprocess.Popen(cmd)

        elif e.control.data == "ld":
            EmulatorSingleton().setEmulator("ld")

            if not path_file.get("LD-Console", False) or not os.path.exists(
                path_file["LD-Console"]
            ):
                self.initial_page.go("/emulator-loading")
                self.initial_page.update()

                if result := find_file_in_all_drives(r"LDPlayer9\\ldconsole\.exe"):
                    path_file["LD-Console"] = result
                    with open("./path.json", "w", encoding="UTF-8") as f:
                        json.dump(path_file, f, indent=2)

            cmd = f"{path_file['LD-Console'].replace('ldconsole', 'adb')} start-server"
            subprocess.Popen(cmd)

        Main(self.initial_page)

    def init(self):
        blue = ft.Container(
            content=ft.Image(
                src=f"bluestacks_logo.png",
                width=70,
                height=70,
                fit=ft.ImageFit.CONTAIN,
            ),
            bgcolor=ft.colors.GREY_900,
            col=6,
            width=100,
            height=100,
            padding=20,
            border=ft.border.all(2, ft.colors.GREY_700),
            on_click=self.go_main,
            data="bluestacks",
        )

        ld = ft.Container(
            content=ft.Image(
                src=f"ld_logo.png",
                width=80,
                height=80,
                fit=ft.ImageFit.CONTAIN,
            ),
            bgcolor=ft.colors.GREY_900,
            col=6,
            width=100,
            height=100,
            padding=20,
            border=ft.border.all(2, ft.colors.GREY_700),
            on_click=self.go_main,
            data="ld",
        )

        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.alignment = ft.CrossAxisAlignment.CENTER

        return self.controls.extend([blue, ld])
