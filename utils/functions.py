import hashlib
import re
import shutil
import subprocess
import sys
from datetime import datetime
from functools import wraps
from os.path import exists
from time import perf_counter

from decohints import decohints

from utils.constants import DEBUG

dir = "./"


def word_to_color(word):
    hash_object = hashlib.sha256()
    hash_object.update(word.encode("utf-8"))
    hex_color = hash_object.hexdigest()[:6]
    return f"#{hex_color}"


def colorize_name(word):
    hex_color = word_to_color(word)
    hex_color = hex_color.lstrip("#")

    text_color_code = f"\033[38;2;{int(hex_color[0:2], 16)};{int(hex_color[2:4], 16)};{int(hex_color[4:6], 16)}m"
    reset_code = "\033[0m"

    return f"{text_color_code}{word}{reset_code}"


def custom_key(item):
    parts = item["instance"].split("_")
    if len(parts) == 1:
        return -1
    return int(parts[1])


def current_time():
    return datetime.now().strftime("%H:%M:%S")


def string_to_co(string):
    pattern_x = r"x=(\d+)"
    pattern_y = r"y=(\d+)"

    matches_x = re.findall(pattern_x, string)
    matches_y = re.findall(pattern_y, string)

    return [
        (int(pair[0]) + 441, int(pair[1]) + 101)
        for pair in list(zip(matches_x, matches_y))
    ]


def string_to_co_slide(string):
    pattern_x = r"x=(\d+)"
    pattern_y = r"y=(\d+)"

    matches_x = re.search(pattern_x, string)
    matches_y = re.search(pattern_y, string)
    # print(matches_y.group())
    return (int(matches_x.group(1)), int(matches_y.group(1)))


def get_time(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        start_time = perf_counter()
        func_output = func(self, *args, **kwargs)
        end_time = perf_counter()

        if 0 and func.__name__ == "check_captcha":
            print(
                f'[ {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} ] [ {self.name} ] Verification made in {(end_time - start_time):0.1f}'
            )
            self.FileSingleton.write(
                self.name,
                f"INFO : Verification made in {(end_time - start_time):0.1f}\n",
            )
        return func_output

    return wrapper


def toString(arg):
    if type(arg).__name__ in ["ndarray", "Image"]:
        return "Image"
    if isinstance(arg, dict):
        return "Dict"
    if callable(arg):
        return arg.__name__
    return repr(arg)


def colorize_output(output):
    if output == repr(True):
        return f"\033[1;32m{output}\033[0m"  # Green color for True
    elif output == repr(False):
        return f"\033[1;31m{output}\033[0m"  # Red color for False
    elif output == "None":
        return f"\033[1;33m{output}\033[0m"  # Yellow color for None
    else:
        return output  # No color for other values


@decohints
def get_name(func):
    @wraps(func)
    def wrapper(self: object, *args: object, **kwargs: object):
        self.script_pause()

        if func.__name__ == "set_timer":
            args_str = [toString(arg) for arg in args] if args is not None else []
            kwargs_str = (
                [f"{key}={toString(value)}" for key, value in kwargs.items()]
                if kwargs is not None
                else []
            )
            arg_str = ", ".join(args_str + kwargs_str)

            timestamp = (
                f"[ \033[1;32m{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\033[0m ]"
            )
            message = f"[ {colorize_name(self.name)} ] {func.__name__}({arg_str})"

            print(f"{timestamp} {message}")

        func_output = func(self, *args, **kwargs)

        if DEBUG:
            args_str = [toString(arg) for arg in args] if args is not None else []
            kwargs_str = (
                [f"{key}={toString(value)}" for key, value in kwargs.items()]
                if kwargs is not None
                else []
            )
            arg_str = ", ".join(args_str + kwargs_str)

            if func_output is True or func_output is False or func_output is None:
                output_str = colorize_output(repr(func_output))
            elif type(func_output).__name__ in ["ndarray", "Image", "str", "int"]:
                output_str = toString(func_output)
            elif hasattr(func_output, "__iter__"):
                output_str = ", ".join([toString(arg) for arg in func_output])
            else:
                output_str = f"Unexpected, {type(func_output)}"

            timestamp = (
                f"[ \033[1;32m{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\033[0m ]"
            )
            message = f"[ {colorize_name(self.name)} ] {func.__name__}({arg_str}): {colorize_output(output_str)}"

            print(f"{timestamp} {message}")

        return func_output

    return wrapper


def get_class(func):
    @wraps(func)
    def wrapper(self: object, *args: object, **kwargs: object):
        self.script_pause()
        func_output = func(self, *args, **kwargs)
        return func_output

    return wrapper


def filter_coordinate(couple: tuple[int, int]):
    if couple[0] < 206:
        return False
    if couple[0] < 274 and couple[1] < 108:
        return False
    if couple[0] > 516 and couple[1] < 168:
        return False
    if couple[0] < 735 and couple[1] > 587:
        return False
    if couple[0] > 1146 and couple[1] < 218:
        return False
    return True


def getchecksum():
    md5_hash = hashlib.md5()
    try:
        file = open("".join(sys.argv), "rb")
    except:
        file = open("".join(sys.argv[0]), "rb")
    md5_hash.update(file.read())
    digest = md5_hash.hexdigest()
    return digest


def get_dic_instances():
    try:
        fileSingleton = FileSingleton()
        path = fileSingleton.get_path()
        string = path["bluestacks"][:-5] + ".txt"
        if exists(rf'{path["bluestacks"]}'):
            string = path["bluestacks"][:-5] + ".txt"
            shutil.copy(rf'{path["bluestacks"]}', rf"{string}")
        with open(rf"{string}", "r", encoding="utf-8") as file:
            data_instance = file.read().split("\n")
    except Exception as e:
        print(e)
        raise OSError(
            "The path you provided is wrong ! We are looking for something like : \n r'C:\ProgramData\BlueStacks_nxt\\bluestacks.conf'"
        )

    pattern_status_adb = re.compile(r"bst\.instance\.Nougat64_?(\d*)\.status\.adb_port")
    pattern_display_name = re.compile(r"bst\.instance\.Nougat64_?(\d*)\.display_name")

    pattern_for_nougat = re.compile(r"Nougat64_?(\d*)")
    pattern_for_value = re.compile(r'="([^"]*)"')

    matched_lines = []

    for line in data_instance:
        line = line.strip()
        # Check for display_name pattern and nougat version
        if pattern_display_name.search(line):
            matched_lines.append(pattern_for_nougat.search(line).group())
            matched_lines.append(pattern_for_value.search(line).group(1))
        # Check for status and adb_port pattern
        elif pattern_status_adb.search(line):
            matched_lines.append(pattern_for_value.search(line).group(1))

    bluestacks_instances = {}
    for i in range(0, len(matched_lines), 3):
        bluestacks_instances[str(matched_lines[i])] = {
            "instance": str(matched_lines[i]),
            "name": matched_lines[i + 1],
            "port": int(matched_lines[i + 2]),
        }

    return bluestacks_instances


def get_index_and_names(data):
    names = []
    for key in data.keys():
        names.append((key, data[key]["name"]))
    return names

def get_dic_instances_ld():
    fileSingleton = FileSingleton()
    path = fileSingleton.get_path()

    argument = "list2"
    command = [path["LD-Console"], argument]
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)

    emulators = result.stdout.split("\n")
    emulators.pop()

    liste = {}
    for emulator in emulators:
        emulator = emulator.split(",")
        liste[emulator[0]] = {
            "name": emulator[1],
            "instance": emulator[0],
            "port": 5554 + 2 * int(emulator[0]),
        }

    return liste


def get_current_instances_ld(data: dict):
    fileSingleton = FileSingleton()
    path = fileSingleton.get_path()

    argument = "runninglist"
    command = [path["LD-Console"], argument]
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)

    emulators = result.stdout.split("\n")
    print(emulators)

    emulators.pop()

    liste = []

    for emulator in emulators:
        for e in data.values():
            if e["name"] == emulator:
                liste.append((e["instance"], e["name"]))
    return liste


# print(get_all_vms_running_ld())
