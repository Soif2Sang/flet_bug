import json
from collections import defaultdict
from datetime import date, datetime
from threading import Lock


class ApiSingleton:
    __instance = None
    FileLock = Lock()
    apikey = ""

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def getApiKey(self) -> str:
        with self.FileLock:
            return self.apikey

    def setApiKey(self, key: str):
        with self.FileLock:
            self.apikey = key


class EmulatorSingleton:
    __instance = None
    FileLock = Lock()
    emulator = ""

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def getEmulator(self) -> str:
        with self.FileLock:
            return self.emulator

    def setEmulator(self, mode: str):
        with self.FileLock:
            self.emulator = mode


class CaptchaSingleton:
    __instance = None
    FileLock = Lock()
    captchas = defaultdict(int)
    tier = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def setTier(self, tier: str) -> None:
        with self.FileLock:
            self.tier = tier

    def getTier(self) -> str:
        with self.FileLock:
            return self.tier

    def getCaptchas(self) -> dict:
        with self.FileLock:
            return self.captchas

    def setCaptchas(self, captchas: dict):
        with self.FileLock:
            self.captchas = captchas

    def addCaptcha(self):
        with self.FileLock:
            self.captchas[datetime.now().date().strftime("%Y-%m-%d")] += 1


class LinkSingleton:
    __instance = None
    FileLock = Lock()
    sellix = ""
    stripe = ""

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def getStripeLink(self) -> str:
        with self.FileLock:
            return self.stripe

    def setStripeLink(self, link: str):
        with self.FileLock:
            self.stripe = link

    def getSellixLink(self) -> str:
        with self.FileLock:
            return self.sellix

    def setSellixLink(self, link: str):
        with self.FileLock:
            self.sellix = link


class FileSingleton:
    __instance = None
    FileLock = Lock()

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def write(self, name, text: str):
        self.FileLock.acquire()
        with open(f"./logs/{name}_logs.txt", "a+", encoding="utf-8") as logger:
            logger.write(f"[ {date.today()} {current_time()} ] [ {name} ] {text}\n")
        self.FileLock.release()

    def get_data(self):
        self.FileLock.acquire()
        with open(f"./user_settings.json", encoding="utf-8") as config_file:
            data = json.load(config_file)
        self.FileLock.release()
        return data

    def get_path(self):
        self.FileLock.acquire()
        with open(f"./path.json", encoding="utf-8") as config_file:
            path = json.load(config_file)
        self.FileLock.release()
        return path

    def write_data(self, data):
        self.FileLock.acquire()
        with open(f"./user_settings.json", "w", encoding="utf-8") as config_file:
            config_file.write(json.dumps(data, indent=2))
        self.FileLock.release()

    def get_default_config(self):
        self.FileLock.acquire()
        with open(f"./default_profile.json", encoding="utf-8") as config_file:
            data = json.load(config_file)
        self.FileLock.release()
        return data


def current_time():
    return datetime.now().strftime("%H:%M:%S")
