import random
import string
import sys
import threading
from random import uniform
from time import sleep

import flet as ft

from utils.functions import current_time, get_name
from views.tiles.handler.config_handler import Frame


class Tile(ft.Row):
    def __init__(self, page, number, **kwargs):
        super().__init__(**kwargs)
        self.number = number
        self.initial_page = page
        self.tasks_process = None
        self.paused = False
        self.stopped = False

        self.runner = Task(self)

        self.tasks_process = threading.Thread(target=self.runner.run)

        self.button_select = ft.IconButton(
            icon=ft.icons.SETTINGS,
            selected_icon=ft.icons.SETTINGS,
            on_click=self.select,
        )
        self.button_start = ft.IconButton(
            icon=ft.icons.PLAY_CIRCLE_OUTLINE_ROUNDED, on_click=self.start
        )
        self.button_stop = ft.IconButton(
            icon=ft.icons.HIGHLIGHT_REMOVE_ROUNDED, disabled=True, on_click=self.stop
        )

        self.text_name = ft.Text(value="nothing", width=80)
        self.text_status = ft.Text(value="", width=120)

        self.vertical_alignment = ft.CrossAxisAlignment.CENTER
        self.alignment = ft.MainAxisAlignment.SPACE_BETWEEN

        self.controls.extend(
            [
                ft.Row(
                    controls=[
                        self.button_select,
                        self.button_start,
                        self.button_stop,
                        self.text_name,
                        self.text_status,
                    ]
                ),
            ]
        )

    def select(self, e):
        self.initial_page.tile_manager.unselect_all()
        self.button_select.selected = True

        if len(self.initial_page.body.controls) > 2:
            self.initial_page.body.controls.pop()

        if self.number not in self.initial_page.frames:
            self.initial_page.frames[self.number] = Frame(
                self.initial_page, self.number
            )

        self.initial_page.body.controls.append(self.initial_page.frames[self.number])
        self.initial_page.update()

    def start(self, e):
        self.button_start.icon = ft.icons.PAUSE
        self.button_stop.disabled = False

        self.paused = False
        self.stopped = False

        self.start_tasks()
        self.button_start.on_click = self.pause
        self.tasks_process.join()
        self.button_start.on_click = self.start
        self.paused = False
        self.stopped = False
        self.button_start.icon = ft.icons.PLAY_CIRCLE_OUTLINE_ROUNDED
        self.button_stop.disabled = True
        self.set_text("")

    def set_text(self, text):
        self.text_status.value = text
        self.initial_page.update()

    def resume(self, e):
        self.paused = False

        self.button_start.icon = ft.icons.PAUSE
        self.initial_page.update()
        self.button_start.on_click = self.pause

    def pause(self, e):
        self.paused = True

        self.button_start.icon = ft.icons.PLAY_CIRCLE_OUTLINE_ROUNDED
        self.button_start.on_click = self.resume
        self.initial_page.update()

    def stop(self, e):
        self.paused = False
        self.stopped = True

        self.button_start.icon = ft.icons.PLAY_CIRCLE_OUTLINE_ROUNDED
        self.button_stop.disabled = True
        self.initial_page.update()

    def start_tasks(self):
        if not self.tasks_process.is_alive():
            self.tasks_process = threading.Thread(target=self.runner.run)
            self.tasks_process.start()

    def get_text(self):
        return self.text_status.value

    def add_text(self, phrase: str, color=None):
        if self.number not in self.initial_page.frames:
            self.initial_page.frames[self.number] = Frame(
                self.initial_page, self.number
            )

        self.initial_page.frames[self.number].add_text(phrase, color)

    def add_divider(self):
        if self.number not in self.initial_page.frames:
            self.initial_page.frames[self.number] = Frame(
                self.initial_page, self.number
            )

        self.initial_page.frames[self.number].add_divider()


class Task():
    def __init__(self, tile):
        self.tile = tile
        self.name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))

    def set_text(self, text, color=None):
        return self.tile.add_text(text, color)

    def set_divider(self):
        return self.tile.add_divider()

    def set_status(self, text):
        return self.tile.set_text(text)

    def debug(self, message):
        print(message)

    def script_pause(self):
        said = False

        while self.tile.paused:
            if not said:
                self.set_text(f"[{current_time()}] Script is paused.", "orange")
                self.debug("Script is paused.")
                said = True
            sleep(0.001)

        if self.tile.stopped:
            self.set_text(f"[{current_time()}] You stopped the bot", "Red")
            self.set_divider()
            self.debug("You stopped the bot")
            sys.exit(1)

        if said:
            self.set_text(f"[{current_time()}] You resumed the script.", "Green")
            self.debug("You resumed the script.")

    @get_name
    def print(self, text: str, color=None) -> None:
        if text != "":
            self.set_text(f"[{current_time()}] {text}", color)
        else:
            self.set_text("")

    @get_name
    def better_sleep(self, limits: tuple[float, float]):
        a = limits[0]
        b = limits[1]

        sleep_duration = uniform(a, b)
        interval_duration = 0.01  # Durée de chaque intervalle (en secondes)
        num_intervals = int(sleep_duration / interval_duration)

        for _ in range(num_intervals):
            sleep(interval_duration)
            self.script_pause()

    @get_name
    def set_timer(self, seconds: int):
        condition = True
        while seconds and condition:
            hours, mins = divmod(seconds, 3600)
            mins, secs = divmod(mins, 60)
            self.set_status(f"{hours:02d}:{mins:02d}:{secs:02d}")
            seconds -= 1
            condition = (
                ":" in self.tile.text_status.value
                and self.tile.text_status.value != "00:00:01"
            )
            self.better_sleep((1, 1))
        self.set_status("")

    def run(self):
        while 1:
            random_number = random.randint(1, 4)
            for i in range(1, random_number):
                self.print(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20)))

            self.better_sleep((0, 1))

            if 1 == random.randint(1, 40):
                self.set_timer(30)
