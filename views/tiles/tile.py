import copy
import random
import string
import sys
import threading
from random import uniform
from time import sleep

import flet as ft

# from tasks.Task import Task
# from tasks.Task_runner import TaskRunner
from utils.functions import FileSingleton, get_all_vms_running, get_all_vms_running_ld, current_time, get_name
from utils.singletons import EmulatorSingleton
from views.tiles.handler.config_handler import Frame


class ConfigOverrider(ft.PopupMenuButton):
    def __init__(self, page, index, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fileSingleton = FileSingleton()
        self.index = index
        self.initial_page = page
        self.config = self.fileSingleton.get_data()[self.index]
        self.icon = ft.icons.FILE_UPLOAD_OUTLINED
        self.init()

    def init(self):
        self.items.append(ft.PopupMenuItem(text="Export Config"))
        self.items.append(ft.PopupMenuItem())
        emulator = EmulatorSingleton().getEmulator()

        if emulator == "bluestacks":
            vms = get_all_vms_running()
        else:
            vms = get_all_vms_running_ld()

        for vm in vms:
            if str(vm[0]) != self.index:
                self.items.append(
                    ft.PopupMenuItem(
                        text=vm[1], on_click=self.override_settings, data=vm[0]
                    )
                )

    def update_config(self):
        self.config = self.fileSingleton.get_data()[self.index]

    def refresh(self):
        self.items = []
        self.init()
        self.initial_page.update()

    def override_settings(self, e):
        self.update_config()
        data = self.fileSingleton.get_data()

        instance = data[str(e.control.data)]["instance"]
        name = data[str(e.control.data)]["name"]
        host = data[str(e.control.data)]["host"]
        port = data[str(e.control.data)]["port"]

        data[str(e.control.data)] = copy.deepcopy(self.config)

        data[str(e.control.data)]["instance"] = instance
        data[str(e.control.data)]["name"] = name
        data[str(e.control.data)]["host"] = host
        data[str(e.control.data)]["port"] = port

        self.fileSingleton.write_data(data)

        if str(e.control.data) in self.initial_page.frames:
            for tab in self.initial_page.frames[str(e.control.data)].settings.tabs:
                tab.content.content.controls = []
                tab.content.init()
        self.initial_page.update()


class Tile(ft.Row):
    def __init__(self, page, number, **kwargs):
        super().__init__(**kwargs)
        self.FileSingleton = FileSingleton()
        data = self.FileSingleton.get_data()
        self.number = number
        self.initial_page = page
        self.tasks_process = None
        self.paused = False
        self.stopped = False

        # self.main_task = Task(self)
        # self.runner = TaskRunner(self.main_task, self)

        self.runner = Task(self)

        if self.initial_page.UPGRADE:
            self.tasks_process = threading.Thread(target=self.runner.run_update)
        else:
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

        self.config_overrider = ConfigOverrider(self.initial_page, number)
        self.text_name = ft.Text(value=data[str(number)]["name"], width=80)
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
                self.config_overrider,
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
            if self.initial_page.UPGRADE:
                self.tasks_process = threading.Thread(target=self.runner.run_update)
            else:
                self.tasks_process = threading.Thread(target=self.runner.run)
            self.tasks_process.start()
        else:
            self.add_text("Task is frozen, you may need to restart the bot.")
            self.initial_page.generate_toast(
                "Warning", "Task is frozen, you may need to restart the bot."
            )
            print("Task is frozen, you may need to restart the bot.")

    def set_text(self, phrase: str):
        self.text_status.value = phrase
        self.initial_page.update()

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
    @get_name
    def set_text(self, text, color=None):
        return self.tile.add_text(text, color)

    @get_name
    def set_divider(self):
        return self.tile.add_divider()

    @get_name
    def set_status(self, text):
        return self.tile.set_text(text)

    @get_name
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

            self.better_sleep((1, 3))

            if 1 == random.randint(1, 40):
                self.set_timer(30)
