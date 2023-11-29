import copy
import os

from utils.functions import FileSingleton


def main():
    fileSingleton = FileSingleton()
    try:
        if not os.path.exists("./user_settings.json"):
            fileSingleton.write_data({})
            print("User settings created")
    except Exception as e:
        print(e)
    try:
        if not os.path.exists("./path.json"):
            fileSingleton.write_data(
                {
                    "bluestacks": "C:\\ProgramData\\BlueStacks_nxt\\bluestacks.conf",
                    "HD-Player": "C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe",
                }
            )
            print("User settings created")
    except Exception as e:
        print(e)

    data = fileSingleton.get_data()

    if "discord" not in data:
        data["discord"] = {"user_id": 0, "enabled": False}
        fileSingleton.write_data(data)

    old_data = copy.deepcopy(data)

    for element in old_data.keys():
        if element.isdigit():
            data[data[element]["instance"]] = copy.deepcopy(data[element])
            del data[element]

    fileSingleton.write_data(data)
