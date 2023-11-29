import shutil
import threading
from os.path import exists

import flet as ft
from tiles.handler.tile_handler import NavigationBar

from tasks.Task import Task
from tasks.Task_runner import TaskRunner
from utils.functions import FileSingleton
from views.tiles.tile_upgrade import TileUpgrade


class TileManagerUpgrade(ft.ListView):
    def __init__(self, page, **kwargs):
        super().__init__(**kwargs)
        self.page = page
        self.initial_page = page

        self.height = 250
        self.expand = 0
        self.tiles: dict[str, TileUpgrade] = {}
        self.navigation_bar: NavigationBar = NavigationBar(self)
        self.controls.append(self.navigation_bar)
        self.start_bar = StartBar(self.initial_page, self)
        # self.controls.append(self.start_bar)
        # self.controls.append(self.logger)

    def add_tile(self, number: str):
        self.tiles[number] = TileUpgrade(self.initial_page, number)
        self.tiles[number].runner = self.start_bar.runner
        self.controls.append(self.tiles[number])

        # self.update()

    def delete_tile(self, number: str):
        index = self.controls.index(self.tiles[number])
        self.controls.pop(index)
        del self.tiles[number]
        self.initial_page.update()

    def update_tiles(self):
        # is_alive = threading.Thread(target=self.process_is_alive)
        # is_alive.deamon = True
        # is_alive.start()
        return

    def unselect_all(self):
        for tile in self.controls[1:]:
            try:
                tile.button_select.selected = False
            finally:
                tile.button_select.update()

    def get_dic_instances(self):
        try:
            path = get_path()
            string = path["bluestacks"][:-5] + ".txt"
            if exists(rf'{path["bluestacks"]}'):
                string = path["bluestacks"][:-5] + ".txt"
                shutil.copy(rf'{path["bluestacks"]}', rf"{string}")
            with open(rf"{string}", "r", encoding="utf-8") as file:
                data_instance = file.read().split("\n")
        except:
            raise OSError(
                "The path you provided is wrong ! We are looking for something like : \n r'C:\ProgramData\BlueStacks_nxt\\bluestacks.conf'"
            )

        def sort_by_instance(tab):
            for i in range(len(tab)):
                for y in range(len(tab) - 1):
                    if len(tab[y]["instance"]) == len(tab[y + 1]["instance"]):
                        if tab[y]["instance"] > tab[y + 1]["instance"]:
                            tab[y], tab[y + 1] = tab[y + 1], tab[y]
                    else:
                        if len(tab[y]["instance"]) > len(tab[y + 1]["instance"]):
                            tab[y], tab[y + 1] = tab[y + 1], tab[y]
            dic = {}
            for i in range(len(tab)):
                dic[str(i)] = tab[i]
            return dic

        liste_info = []
        for element in data_instance:
            if (
                (("bst.instance.Nougat64" in element) and ("adb_port" in element))
                and "status" in element
            ) or (("bst.instance.Nougat64" in element) and ("display_name" in element)):
                liste_info.append(element)
        tab_instance = []
        for i in range(0, len(liste_info), 2):
            string = liste_info[i + 1].split(".status.adb_port=")

            instance = string[0].split(".")[-1]
            port = string[1].replace('"', "")
            display_name = liste_info[i].split(".display_name=")[1].replace('"', "")

            dico_instance = {
                "instance": str(instance),
                "port": port,
                "name": display_name,
            }
            tab_instance.append(dico_instance)
        return sort_by_instance(tab_instance)

    def get_names(self, data):
        names = []
        for key in data.keys():
            for element in data[key]:
                if element == "name":
                    names.append((len(names), data[key][element]))
        return names

    def get_current_instances(self, data):
        names = self.get_names(data)
        # print(f"{names = }")
        # print(names)
        # instances_available = []
        # for win in pyautogui.getAllWindows():
        #     for name in names:
        #         if win.title == name[1]:
        #             instances_available.append(name)
        # print(instances_available)
        names.sort(key=lambda x: x[0])
        # print(instances_available)
        return names

    def get_all_vms_running(self):
        return self.get_current_instances(self.get_dic_instances())

    def refresh(self):
        data = get_data()

        instances = self.get_dic_instances()
        print(instances)
        for key in instances:
            default_dic = {
                "instance": instances[str(key)]["instance"],
                "name": instances[str(key)]["name"],
                "host": "127.0.0.1",
                "port": int(instances[str(key)]["port"]),
                "API_KEY": "",
                "loop_task": False,
                "time_to_wait_loop1": 60,
                "time_to_wait_loop2": 110,
                "leave_game_loop": True,
                "scheduler": False,
                "schedules": {},
            }
            for i in range(1, 4):
                default_dic["schedules"][i] = {
                    "enabled": False,
                    "kingdom": 0,
                    "city_x": 0,
                    "city_y": 0,
                    "radius": 30,
                    "First": "stone",
                    "Second": "food",
                    "Third": "gold",
                    "Fourth": "wood",
                    "Fifth": "food",
                    "Sixth": "food",
                    "Seventh": "food",
                    "First_level": 6,
                    "Second_level": 6,
                    "Third_level": 6,
                    "Fourth_level": 6,
                    "Fifth_level": 6,
                    "Sixth_level": 6,
                    "Seventh_level": 6,
                    "rss_custom_preset": False,
                    "auto_reconnect": True,
                    "auto_captcha": True,
                    "check_donation": False,
                    "use_enhanced_buff": False,
                    "gather_rss": False,
                    "buy_merchant": False,
                    "claim_daily_quests": False,
                    "collect_ressource": False,
                    "defeat_barbarians": False,
                    "barbarians_level": 25,
                    "gather_gem": False,
                    "gem_check1": 60,
                    "gem_check2": 120,
                    "gem_experimental": False,
                    "gather_gem_duration1": 60,
                    "gather_gem_duration2": 90,
                    "restart_game": False,
                    "switch_character": False,
                    "leave_game_switch_character": False,
                    "scout_fog": False,
                    "scout_duration1": 60,
                    "scout_duration2": 90,
                    "slow_mode": False,
                    "sleep_multiplicator": 1,
                    "auto_log_back": True,
                    "log_back1": 5,
                    "log_back2": 10,
                    "claim_daily_vip": False,
                    "claim_daily_chest": False,
                    "claim_campaign": False,
                    "start_fort": False,
                    "rally_type": "cav",
                    "rally_time": 10,
                    "rally_radius": 20,
                    "rally_count": 2,
                    "mauraudeurs_forts": False,
                    "heal_troop": False,
                    "healing_building_x": 980,
                    "healing_building_y": 267,
                    "healing_count": 1500,
                    "material_production": False,
                    "material_choice_1": "leather",
                    "material_choice_2": "leather",
                    "material_choice_3": "leather",
                    "material_choice_4": "leather",
                    "material_choice_5": "leather",
                    "alliance_help": False,
                    "train_troops": False,
                    "infantry_camp": [],
                    "cavalry_camp": [],
                    "archery_camp": [],
                    "siege_camp": [],
                    "hospital": None,
                    "scout_camp": [],
                    "infantry_enable": True,
                    "cavalry_enable": True,
                    "archery_enable": True,
                    "siege_enable": True,
                    "infantry_tier": "t1",
                    "cavalry_tier": "t1",
                    "archery_tier": "t1",
                    "siege_tier": "t1",
                    "city_transfer": [],
                    "transfer_enable": False,
                    "transfer_food": 0,
                    "transfer_wood": 0,
                    "transfer_stone": 0,
                    "transfer_gold": 0,
                }
            if str(key) not in data:
                default_dic["schedules"][1]["enabled"] = True
                data[str(key)] = default_dic
            else:
                for key2 in default_dic:
                    if key2 not in data[str(key)]:
                        data[str(key)][key2] = default_dic[key2]

                for key2 in default_dic["schedules"][1]:
                    for i in range(1, 4):
                        if key2 not in data[str(key)]["schedules"][str(i)]:
                            data[str(key)]["schedules"][str(i)][key2] = default_dic[
                                "schedules"
                            ][1][key2]
            data[str(key)]["instance"] = instances[str(key)]["instance"]
            data[str(key)]["name"] = instances[str(key)]["name"]
            data[str(key)]["port"] = int(instances[str(key)]["port"])
        print(f"Before refresh")
        for key in data:
            print(key, end=", ")
        write_data(data)
        data_previous = data
        data = get_data()
        print(f"\nAfter refresh")
        for key in data:
            print(key, end=", ")
        instances = self.get_all_vms_running()

        for i in range(len(self.controls) - 1):
            self.controls.pop()
        for instance in instances:
            if str(instance[0]) in self.tiles:
                self.controls.append(self.tiles[str(instance[0])])
            else:
                self.add_tile(str(instance[0]))
        self.update()

    def add_text(self, phrase, color):
        self.page.logger.add_text(phrase, color)

    def get_enabled_sel(self):
        tiles = []
        for tile in self.controls[1:]:
            if tile.selected:
                tiles.append(tile.number)
        return tiles


class StartBar(ft.Row):
    def __init__(self, page, tile_manager: TileManagerUpgrade, **kwargs):
        super().__init__(**kwargs)
        self.text_status = ft.Text()
        self.number = 0
        self.main_task = Task(self)
        self.runner = TaskRunner(self.main_task, self)
        self.tasks_process = threading.Thread(target=self.runner.run3)

        self.page = page
        self.tile_manager = tile_manager
        self.started = False
        self.stopped = False

        self.button_start = ft.IconButton(
            icon=ft.icons.NOT_STARTED_OUTLINED, on_click=lambda _: self.start()
        )
        self.button_stop = ft.IconButton(
            icon=ft.icons.STOP_OUTLINED, disabled=True, on_click=lambda _: self.stop()
        )

        self.controls.extend([self.button_start, self.button_stop, self.text_status])

    def get_enabled_sel(self):
        return self.tile_manager.get_enabled_sel()

    def start(self):
        self.started = not self.started
        self.stopped = False
        if self.started:
            self.button_start.icon = ft.icons.PAUSE
            self.button_stop.disabled = False
        else:
            self.button_start.icon = ft.icons.NOT_STARTED_OUTLINED
            self.button_stop.disabled = False
        self.start_tasks()
        self.button_start.update()
        self.button_stop.update()

    def process_is_alive(self):
        self.tasks_process.join()
        self.started = False
        self.stopped = False
        self.button_start.icon = ft.icons.NOT_STARTED_OUTLINED
        self.button_stop.disabled = True
        self.button_start.update()
        self.button_stop.update()

    def start_tasks(self):
        if not self.tasks_process.is_alive():
            self.tasks_process = threading.Thread(target=self.runner.run3)
            self.tasks_process.daemon = True
            self.tasks_process.start()
        else:
            print("Task is running")

    def stop(self):
        self.started = False
        self.stopped = True
        self.button_start.icon = ft.icons.NOT_STARTED_OUTLINED
        self.button_stop.disabled = True
        self.set_text("")
        self.button_start.update()
        self.button_stop.update()

    def set_text(self, phrase: str):
        self.text_status.value = phrase
        self.text_status.update()

    def get_text(self):
        return self.text_status.value

    def add_text(self, phrase: str, color=None):
        self.tile_manager.add_text(phrase, color)
