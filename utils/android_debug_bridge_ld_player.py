import io
import shutil
import subprocess
import traceback
from datetime import date
from os.path import exists
from time import sleep

import pytesseract as tess
from cv2 import (
    COLOR_BGR2HSV,
    COLOR_BGR2RGB,
    TM_CCOEFF_NORMED,
    cvtColor,
    inRange,
    matchTemplate,
    minMaxLoc,
)
from numpy import array, ndarray, where
from PIL import Image
from ppadb.client import Client as PPADBClient

from utils.functions import FileSingleton, current_time, get_dic_instances_ld
from utils.resources import ImageSingleton

bridge = None


class AdbLd:
    def __init__(self, number: str, host="127.0.0.1", port=5037):
        self.FileSingleton = FileSingleton()
        self.data = self.FileSingleton.get_data()
        self.client = PPADBClient(host, port)
        self.host = host
        self.port = port
        self.number = number
        self.name = self.data[str(self.number)]["name"]
        self.images = ImageSingleton()
        self.is_ld = True

    def __str__(self):
        print(f"JsonNumber:{self.number} port:{self.port}")
        return f"JsonNumber:{self.number} port:{self.port}"

    def update_port(self):
        instances = get_dic_instances_ld()

        if str(self.number) not in instances:
            return

        if self.port != int(instances[str(self.number)]["port"]):
            self.data = self.FileSingleton.get_data()
            self.data[str(self.number)]["instance"] = instances[str(self.number)][
                "instance"
            ]
            self.data[str(self.number)]["name"] = instances[str(self.number)]["name"]
            self.data[str(self.number)]["port"] = int(
                instances[str(self.number)]["port"]
            )
            self.port = int(instances[str(self.number)]["port"])
            self.FileSingleton.write_data(self.data)

    def connect_to_device(self, host="emulator"):
        path = self.FileSingleton.get_path()
        self.update_port()

        adb_path = f"{path['LD-Console'].replace('ldconsole', 'adb')} start-server"
        cmd = f"{adb_path} connect {host}-{self.port}"
        subprocess.Popen(cmd)

    def get_client_devices(self):
        return self.client.devices()

    def get_device(self, host="emulator", fail=0):
        try:
            self.port = str(self.data[str(self.number)]["port"])
            device = self.client.device(f"{host}-{self.port}")
            # print(device)
            if device is None:
                self.print(f"INFO : Device is None, trying to reconnect..")
                self.connect_to_device()
                sleep(2)

                if device is None and fail > 45:
                    return
                if device is None:
                    return self.get_device()
            # print(device)
            return device
        except Exception as e:
            traceback.print_exc()
            self.print("EXCEPTION : Error in connect to device")

            self.update_port()
            path = self.FileSingleton.get_path()
            cmd = f"{path['LD-Console'].replace('ldconsole', 'adb')} start-server"
            subprocess.Popen(cmd)

            self.print(f"Adb restarting..")
            sleep(20)
            self.print(f"Connecting to the device..")

            self.connect_to_device()

            sleep(5)
            return self.get_device()

    def print(self, text: str):
        data = self.FileSingleton.get_data()
        print(
            f"[ {date.today()} {current_time()} ] [ {data[str(self.number)]['name']} ] {text}"
        )
        self.FileSingleton.write(self.name, text)

    def get_curr_device_screen_img_byte_array(self):
        try:
            return self.get_device().screencap()
        except Exception as e:
            print(e)
            sleep(1)
            return self.get_device().screencap()

    def get_curr_device_screen_img_bytesIO(self):
        try:
            return io.BytesIO(self.get_device().screencap())
        except Exception as e:
            print(e)
            sleep(1)
            return io.BytesIO(self.get_device().screencap())

    def get_curr_device_screen_img(self, deadstop=0):
        try:
            device = self.get_device()
            if device is None:
                print("get_curr_device_screen_img device is null")
                self.connect_to_device()
            output = io.BytesIO(device.screencap())
            # output.seek(0)
            image = Image.open(output)
            # self.print("INFO : Image opened")
            return image
        except Exception as e:
            self.print(f"EXCEPTION : get_screen_device")
            if deadstop == 30:
                raise e
            sleep(1)
            self.connect_to_device()
            return self.get_curr_device_screen_img(deadstop + 1)

    def get_cv2_img(self):
        try:
            screen = self.get_curr_device_screen_img()
            screen = array(screen)
            screen = cvtColor(screen, COLOR_BGR2RGB)
            return screen
        except:
            sleep(1)
            screen = self.get_curr_device_screen_img()
            screen = array(screen)
            screen = cvtColor(screen, COLOR_BGR2RGB)
            return screen

    def save_screen(self, file_name):
        image = Image.open(io.BytesIO(self.get_device().screencap()))
        image.save(f".//{file_name}.png")
        return True

    def find_img_cv(self, img_to_find, confidence=0.9):
        pil_image = self.get_curr_device_screen_img()
        cv_image = array(pil_image)
        cv_image = cvtColor(cv_image, COLOR_BGR2RGB)
        result = matchTemplate(cv_image, img_to_find, TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = minMaxLoc(result)
        if max_val > confidence:
            return max_loc[0], max_loc[1]
        else:
            return

    def find_img(self, target: str, source: ndarray = None, confidence=0.9):
        try:
            if source is None:
                pil_image = self.get_curr_device_screen_img()
                source = array(pil_image)
                if target == "new_troops_button":
                    source = source[0:322, 800:1280]
                if target == "gem_search_button":
                    source = source[470:600, 0:150]

                source = cvtColor(source, COLOR_BGR2RGB)

            img_to_find = self.images.get_file_name(target)
            # bot.adb.get_cv2_img()
            result = matchTemplate(source, img_to_find, TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = minMaxLoc(result)
            if max_val > confidence:
                if target == "new_troops_button":
                    return max_loc[0] + 800, max_loc[1]
                return max_loc[0], max_loc[1]
            else:
                return
        except Exception as exception_error:
            self.print("Error occured when using find_image")
            self.print(target)
            traceback.print_exc()
            self.print(exception_error)

    def find_img_src_conf(self, src, target, confidence):
        img_to_find = self.images.get_file_name(target)
        result = matchTemplate(src, img_to_find, TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = minMaxLoc(result)
        if max_val > confidence:
            return max_loc[0], max_loc[1]
        else:
            return

    def find_multiple_img(self, target, source=None, confidence=0.9):
        if source is None:
            pil_image = self.get_curr_device_screen_img()
            cv_image = array(pil_image)
            source = cvtColor(cv_image, COLOR_BGR2RGB)
        cv_image = source

        img_to_find = self.images.get_file_name(target)
        if target == "back_icon":
            cv_image = cv_image[0:720, 1000:1280]
        # print(img_to_find)
        result = matchTemplate(cv_image, img_to_find, TM_CCOEFF_NORMED)
        needle_w = img_to_find.shape[1]
        needle_h = img_to_find.shape[0]

        min_val, max_val, min_loc, max_loc = minMaxLoc(result)
        min_thresh = confidence
        # print(min_thresh>confidence)
        location = where(result >= min_thresh)
        location = list(zip(*location[::-1]))
        # print(location)

        rectangles = []
        for loc in location:
            rect = [int(loc[0]), int(loc[1]), needle_w, needle_h]
            rectangles.append(rect)
        # print(rectangles)

        localisations = []

        for i in range(len(rectangles)):
            if target == "back_icon":
                # print(file_name)
                # print(rectangles[i][0])
                # print(rectangles[i][0]+1000)
                localisations.append((rectangles[i][0] + 1000, rectangles[i][1]))
            else:
                localisations.append((rectangles[i][0], rectangles[i][1]))
        element_to_delete = []
        for i in range(len(localisations) - 1):
            if (
                (localisations[i][0] + 1 == localisations[i + 1][0])
                or (localisations[i][0] - 1 == localisations[i + 1][0])
                or (localisations[i][0] == localisations[i + 1][0])
            ) and (
                (localisations[i][1] + 1 == localisations[i + 1][1])
                or (localisations[i][1] - 1 == localisations[i + 1][1])
                or (localisations[i][1] == localisations[i + 1][1])
            ):
                element_to_delete.append(localisations[i])

        # print(element_to_delete)
        for element in element_to_delete:
            localisations.remove(element)
        return localisations

    def is_game_alive(self):
        string = "dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp'"
        a = self.shell(string)
        return "lilithgame" in a or "rok" in a or "lilithgames" in a

    def click(self, x, y):
        string = f"input tap {x} {y}"
        self.shell(string)
        return

    def shell(self, string):
        device = self.get_device()
        try:
            return device.shell(string)
        except RuntimeError:
            print("Cannot use shell")
            sleep(3)
            self.connect_to_device()
            return self.shell(string)

    def swipe(self, x, y, x2, y2):
        string = f"input swipe {x} {y} {x2} {y2} 420"
        self.shell(string)
        return

    def swipe_arg(self, x, y, x2, y2, arg):
        string = f"input swipe {x} {y} {x2} {y2} {arg}"
        self.shell(string)
        return

    #
    # def resource_amount_image_to_string(self):
    #     result_list = []
    #     boxes = [
    #         (695, 10, 770, 34), (820, 10, 890, 34), (943, 10, 1015, 34), (1065, 10, 1140, 34)]
    #     for box in boxes:
    #         x0, y0, x1, y1 = box
    #         imsch = imdecode(asarray(self.get_curr_device_screen_img_byte_array(), dtype=uint8),
    #                          IMREAD_COLOR)
    #         imsch = imsch[y0:y1, x0:x1]
    #         resource_image = Image.fromarray(imsch)
    #         try:
    #             result_list.append(abs(int(img_to_string(resource_image)
    #                                        .replace('.', '')
    #                                        .replace('B', '00000000')
    #                                        .replace('M', '00000')
    #                                        .replace('K', '00')
    #                                        ))
    #                                )
    #         except Exception as e:
    #             result_list.append(-1)
    #     return result_list

    def restart_emulator(self):
        try:
            path = self.FileSingleton.get_path()
            string = path["bluestacks"][:-5] + ".txt"
            if exists(rf'{path["bluestacks"]}'):
                string = path["bluestacks"][:-5] + ".txt"
                shutil.copy(rf'{path["bluestacks"]}', rf"{string}")

            with open(rf"{string}", "r") as file:
                data_instance = file.read().split("\n")
        except:
            print(
                "The pass you provided is wrong ! We are looking for something like : \n C:\ProgramData\BlueStacks_nxt\bluestacks.conf"
            )

        liste_info = []
        for element in data_instance:
            if (
                (("bst.instance.Nougat64" in element) and ("adb_port" in element))
                and "status" not in element
            ) or (("bst.instance.Nougat64" in element) and ("display_name" in element)):
                liste_info.append(element)

        dico_instance = {}
        for i in range(0, len(liste_info), 2):
            string = liste_info[i].split(".adb_port=")
            string[1] = string[1].replace('"', "")
            string[0] = string[0][13:]
            dico_instance[str(len(dico_instance))] = {}
            dico_instance[str(len(dico_instance) - 1)]["instance"] = str(string[0])
            dico_instance[str(len(dico_instance) - 1)]["port"] = string[1]
            string2 = liste_info[i + 1].split(".display_name=")
            string2[1] = string2[1].replace('"', "")
            dico_instance[str(len(dico_instance) - 1)]["name"] = string2[1]

    def home_button(self):
        self.shell("input keyevent KEYCODE_HOME")

    #
    # def enable_adb(self,host='127.0.0.1', port=5037):
    #     adb = None
    #     try:
    #         adb = Adb(host=host, port=port)
    #
    #         version = adb.client.version()
    #
    #         if version != 41:
    #             raise RuntimeError('Error: require adb version 41, but version is {}'.format(version))
    #
    #     except RuntimeError as err:
    #         with open('path.json') as config_file:
    #             path = json.load(config_file)
    #         adb_path = f"{path['HD-Player'].replace('Player', 'Adb')}"
    #         # adb_path = r"C:\Program Files\BlueStacks_nxt\HD-Adb.exe"
    #
    #         ret = subprocess.run(f"{adb_path} -P {port} kill-server {host}", shell=True,
    #                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    #
    #         ret = subprocess.run(f"{adb_path} -P {port} connect {host}", shell=True,
    #                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    #
    #         if ret.returncode != 0:
    #             raise RuntimeError('Error: fail to start adb server. \n({})'.format(ret))
    #
    #     return adb


def img_to_string(pil_image):
    # pil_image.save(resource_path("test.png"))
    tess.pytesseract.tesseract_cmd = "tesseract\\tesseract.exe"
    result = (
        tess.image_to_string(pil_image, lang="eng", config="--psm 6")
        .replace("\t", "")
        .replace("\n", "")
        .replace("\f", "")
    )
    return result


def img_remove_background_and_enhance_word(cv_image, lower, upper):
    hsv = cvtColor(cv_image, COLOR_BGR2HSV)
    return inRange(hsv, lower, upper)
