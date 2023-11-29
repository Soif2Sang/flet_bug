import json
import os
import re

import win32api

from utils.functions import FileSingleton


def find_file(root_folder, rex):
    for root, dirs, files in os.walk(root_folder):
        for f in files:
            path = os.path.join(root, f)
            result = rex.search(path)
            if result:
                return path


def find_file_in_all_drives(file_name):
    # create a regular expression for the file
    rex = re.compile(file_name)
    for drive in win32api.GetLogicalDriveStrings().split("\000")[:-1]:
        if result := find_file(drive, rex):
            return result


import flet as ft


class RowFinder(ft.Row):
    def __init__(self, mot, **kwargs):
        super().__init__(**kwargs)
        self.FileSingleton = FileSingleton()
        self.path_json = self.FileSingleton.get_path()
        self.mot = mot
        self.enhanced_mot = self.mot.split("\\")[0]
        self.text = ft.Text(value=f"Set {self.enhanced_mot} file location")
        self.entry = ft.TextField(
            value=self.path_json[self.mot.split("\\")[0]], width=400
        )
        file_picker = ft.FilePicker(on_result=self.on_dialog_result)
        self.controls.append(file_picker)
        self.choice = ft.ElevatedButton(
            "Set file manually...",
            on_click=lambda _: file_picker.pick_files(allow_multiple=False),
        )
        self.script = ft.ElevatedButton(
            text="Let the script find it..", on_click=lambda e: self.find(e)
        )

        self.controls.extend([self.text, self.entry, self.choice, self.script])

    def close_banner(self, e):
        self.page.banner.open = False
        self.page.update()

    def pop_banner(self, text, color=ft.colors.AMBER_100):
        self.page.banner = ft.Banner(
            bgcolor=color,
            content=ft.Text(value=text),
            actions=[
                ft.TextButton("Ok", on_click=self.close_banner),
            ],
            open=True,
        )
        if color == ft.colors.AMBER_100:
            self.page.banner.leading = ft.Icon(
                ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40
            )

        self.page.update()

    def on_dialog_result(self, e: ft.FilePickerResultEvent):
        print("Selected files:", e.files[0].path)
        print("Selected file or directory:", e.path)
        self.path_json[self.mot.split("\\")[0]] = e.files[0].path
        self.path_json = self.FileSingleton.get_path()
        self.entry.value = e.files[0].path
        self.update()

    def find(self, e):
        if result := find_file_in_all_drives(self.mot):
            self.path_json[self.mot.split("\\")[0]] = result
            with open("../path.json", "w", encoding="UTF-8") as f:
                json.dump(self.path_json, f, indent=2)
            self.entry.value = result
            self.pop_banner("Success", "green")
            self.update()
        else:
            self.pop_banner("Unable to locate the file")
            print("Unable to locate the file")


def main(page: ft.Page):
    page.window_height = 230
    page.window_width = 1000

    def on_dialog_result(e: ft.FilePickerResultEvent):
        print("Selected files:", e.files)
        print("Selected file or directory:", e.path)

    # file_picker = ft.FilePicker(on_result=on_dialog_result)
    # page.add(file_picker)
    #
    # button = ft.ElevatedButton("Choose files...",
    #                   on_click=lambda _: file_picker.pick_files(allow_multiple=False))
    #
    # page.add(button)
    page.add(RowFinder("bluestacks\.conf"))
    page.add(RowFinder("HD-Player\.exe"))
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
# print(find_file_in_all_drives( 'bluestacks\.conf' ))
