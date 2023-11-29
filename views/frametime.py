from datetime import datetime, timedelta
from random import randint

import flet as ft

from utils.Components.card import GenerateCard
from utils.flet_translations import translate
from utils.functions import FileSingleton

color_bank = {1: "#3b8ed0", 2: "#ba4543", 3: "#dec433"}


def is_valid_time(time_str):
    try:
        hours, minutes = map(int, time_str.split(":"))
        if 0 <= hours <= 23 and 0 <= minutes <= 59:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def is_in_frametime(first, second):
    current_time = datetime.now().time()
    start_time = datetime.strptime(first, "%H:%M").time()
    end_time = datetime.strptime(second, "%H:%M").time()

    if start_time < end_time:
        return start_time <= current_time <= end_time
    else:
        now = datetime.now()
        midnight = datetime.combine(now.date(), datetime.min.time()) + timedelta(days=1)
        time_remaining = midnight - now

        # Calculate the end_time adjusted for the remaining time until the next day
        adjusted_end_time = (
            midnight + timedelta(seconds=time_remaining.seconds)
        ).time()

        return start_time <= current_time <= adjusted_end_time


def random_time_in_frametime(first, second):
    if is_valid_time(first) and is_valid_time(second):
        start_time = datetime.strptime(first, "%H:%M").time()
        end_time = datetime.strptime(second, "%H:%M").time()

        if start_time < end_time:
            time_diff = (
                datetime.combine(datetime.min, end_time)
                - datetime.combine(datetime.min, start_time)
            ).total_seconds()
        else:
            time_diff = (
                datetime.combine(datetime.min, end_time)
                + timedelta(days=1)
                - datetime.combine(datetime.min, start_time)
            ).total_seconds()

        random_seconds = randint(0, int(time_diff))

        new_time = (
            datetime.combine(datetime.min, start_time)
            + timedelta(seconds=random_seconds)
        ).time()

        return random_seconds

    return "Invalid Time"


class RowTimezone(ft.Row):
    def __init__(
        self,
        instance,
        profile,
        parent,
        start="00:00",
        end="00:00",
        default=True,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.FileSingleton = FileSingleton()
        self.data = self.FileSingleton.get_data()
        if start == "00:00" and end == "00:00" and default:
            self.data[str(instance)]["schedules"][str(profile)]["timing"].append(
                ["00:00", "00:00"]
            )
        self.instance = str(instance)
        self.profile = str(profile)
        self.parent = parent
        self.start = start
        self.stop = end
        self.field_start = ft.TextField(
            label="Start",
            value=start,
            on_submit=lambda _: self.sub(),
            height=50,
            width=100,
        )
        self.field_stop = ft.TextField(
            label="End", value=end, on_submit=lambda _: self.sub(), height=50, width=100
        )
        self.delete = ft.IconButton(
            icon=ft.icons.DELETE_FOREVER_ROUNDED,
            icon_color="pink600",
            icon_size=40,
            tooltip="Delete",
            on_click=lambda _: self.parent.delete(self),
        )
        self.controls.extend([self.field_start, self.field_stop, self.delete])
        self.FileSingleton.write_data(self.data)

    def close_banner(self, e):
        self.page.banner.open = False
        self.page.update()

    def pop_banner(self, text):
        self.page.banner = ft.Banner(
            bgcolor=ft.colors.AMBER_100,
            leading=ft.Icon(
                ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40
            ),
            content=ft.Text(value=text),
            actions=[
                ft.TextButton("Ok", on_click=self.close_banner),
            ],
            open=True,
        )

        self.page.update()

    def sub(self):
        self.data = self.FileSingleton.get_data()
        i = self.data[self.instance]["schedules"][self.profile]["timing"].index(
            [self.start, self.stop]
        )

        self.data[self.instance]["schedules"][self.profile]["timing"][i] = [
            self.field_start.value,
            self.field_stop.value,
        ]
        if not is_valid_time(self.field_start.value) or not is_valid_time(
            self.field_stop.value
        ):
            self.pop_banner("Wrong format, please fix")
        else:
            self.start, self.stop = self.field_start.value, self.field_stop.value
            self.FileSingleton.write_data(self.data)


class ManagerTimezone(ft.ListView):
    def __init__(self, instance, profile, **kwargs):
        super().__init__(**kwargs)
        self.FileSingleton = FileSingleton()
        self.data = self.FileSingleton.get_data()
        self.instance = str(instance)
        self.profile = str(profile)
        self.spacing = 10
        self.expand = True
        # self.controls.append(ft.Text(value="Welcome to Profile Activation Settings!\n"
        #                                    "You have the flexibility to set multiple activation frametimes for your profile.\n"
        #                                    "When entering the time, please use the 'hours:minutes' format, following a 24-hour clock notation.\nFor example, 02:00 pm should be entered as 14:00, aligning with your computer's 24-hour clock time.\n"
        #                                    "It's essential to adjust your re-do task timings carefully to avoid unintentionally running the profile twice during the same frametime.\n\n"
        #                                    "Enjoy the power of customizing your profile activation schedule!"))
        val = translate(
            "The time format should be 'hh:mm' and work on a 24-hour clock and on your computer clock.\nexemple:\n     - start : 02:00 / end : 04:00 means the script will start exclusively between 02:00 and 04:00."
        )
        self.controls.append(GenerateCard(subtitle=val, level="notice", height=None))
        self.controls.append(
            ft.Row(
                controls=[
                    ft.Switch(
                        label=translate("Enable profile frametime"),
                        active_track_color=color_bank[int(self.profile)],
                        value=True
                        if self.data[str(self.instance)]["schedules"][
                            str(self.profile)
                        ]["enable_timing"]
                        else False,
                        on_change=lambda _: self.reverse_keyword("enable_timing"),
                    ),
                    ft.ElevatedButton(
                        text=translate("Add new rule"),
                        on_click=lambda _: self.add_tile(),
                        icon=ft.icons.ADD,
                    ),
                ],
                spacing=50,
            )
        )
        self.init()

    def reverse_keyword(self, keyword: str, index=None):
        if index is None:
            index = self.profile
        self.data[str(self.instance)]["schedules"][str(index)][keyword] = not self.data[
            str(self.instance)
        ]["schedules"][str(index)][keyword]
        self.FileSingleton.write_data(self.data)

    def init(self):
        for tup in self.data[self.instance]["schedules"][self.profile]["timing"]:
            self.controls.append(
                RowTimezone(
                    self.instance,
                    self.profile,
                    self,
                    start=tup[0],
                    end=tup[1],
                    default=False,
                )
            )

    def add_tile(self, refresh=True):
        self.data = self.FileSingleton.get_data()
        self.controls.append(RowTimezone(self.instance, self.profile, self))
        self.update()

    def delete(self, tile):
        self.data = self.FileSingleton.get_data()
        self.data[self.instance]["schedules"][self.profile]["timing"].pop(
            self.data[self.instance]["schedules"][self.profile]["timing"].index(
                [tile.start, tile.stop]
            )
        )

        for i in range(len(self.controls)):
            if self.controls[i] == tile:
                self.controls.pop(i)
                break
        self.FileSingleton.write_data(self.data)
        self.update()


global sel, profile


def main(page: ft.Page):
    page.window_width = 720
    page.window_height = 430

    page.add(ManagerTimezone(sel, profile))
    page.title = f"Profile n°{profile} configuration"
    page.update()


def start(sel_param="1", profile_param="1"):
    global sel, profile
    sel = sel_param
    profile = profile_param
    ft.app(target=main)


if __name__ == "__main__":
    # start()
    timings = ["9:00", "23:00"]
    print(random_time_in_frametime(*timings))
