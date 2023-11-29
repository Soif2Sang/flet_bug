import binascii  # hex encoding
import json as jsond  # json
import os
import platform  # check platform
import subprocess  # needed for mac device
import time  # sleep before exit
from threading import Lock
from uuid import uuid4  # gen random guid

import flet as ft
import requests
import win32security
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad

from utils.constants import BREZILIAN
from utils.functions import FileSingleton
from utils.singletons import ApiSingleton, LinkSingleton

fileSingleton = FileSingleton()


def update_user_info(password, username):
    data = fileSingleton.get_data()
    data["user"] = {"username": username, "password": password}
    fileSingleton.write_data(data)


def kill_app():
    os.system("taskkill /f /im flet.exe >nul 2>&1")
    time.sleep(3)
    os._exit(1)


try:  # Connection check
    s = requests.Session()  # Session
    response = s.get("https://httpbin.org/ip")
    data = response.json()
    public_ip = data["origin"]
except requests.exceptions.RequestException as e:
    print(e)
    kill_app()


class selfApi:
    name = ownerid = secret = version = hash_to_check = ""

    def __init__(self, name, ownerid, secret, version, hash_to_check, page=None):
        self.name = name

        self.ownerid = ownerid

        self.secret = secret
        self.version = version
        self.hash_to_check = hash_to_check

        self.page = page

        self.init()

    sessionid = enckey = ""
    initialized = False

    def init(self):
        if self.sessionid != "":
            print("You've already initialized!")
            kill_app()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()

        self.enckey = SHA256.new(str(uuid4())[:8].encode()).hexdigest()

        post_data = {
            "type": binascii.hexlify("init".encode()),
            "ver": encryption.encrypt(self.version, self.secret, init_iv),
            "hash": self.hash_to_check,
            "enckey": encryption.encrypt(self.enckey, self.secret, init_iv),
            "name": binascii.hexlify(self.name.encode()),
            "ownerid": binascii.hexlify(self.ownerid.encode()),
            "init_iv": init_iv,
        }

        response = self.__do_request(post_data)

        if response == "KeyAuth_Invalid":
            print("The application doesn't exist")
            kill_app()

        response = encryption.decrypt(response, self.secret, init_iv)
        json = jsond.loads(response)

        if json["message"] == "invalidver":
            if json["download"] != "":
                print("New Version Available")
                download_link = json["download"]
                os.system(f"start {download_link}")
                kill_app()
            else:
                print(
                    "Invalid Version, Contact owner to add download link to latest app version"
                )
                kill_app()

        if not json["success"]:
            print(json["message"])
            kill_app()

        self.sessionid = json["sessionid"]
        self.initialized = True
        self.__load_app_data(json["appinfo"])

    def login(self, user, password, hwid=None, page=None):
        self.checkinit()
        if hwid is None:
            hwid = others.get_hwid()

        if page is not None and self.page is None:
            self.page = page

        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()

        post_data = {
            "type": binascii.hexlify("login".encode()),
            "username": encryption.encrypt(user, self.enckey, init_iv),
            "pass": encryption.encrypt(password, self.enckey, init_iv),
            "sessionid": binascii.hexlify(self.sessionid.encode()),
            "name": binascii.hexlify(self.name.encode()),
            "ownerid": binascii.hexlify(self.ownerid.encode()),
            "init_iv": init_iv,
        }

        response = self.__do_request(post_data)
        response = encryption.decrypt(response, self.enckey, init_iv)

        self.log(f"Trying to login IP : {public_ip}; HWID : {hwid}")
        json = jsond.loads(response)
        wid1 = self.getvar("HWID1")
        wid2 = self.getvar("HWID2")

        if wid1 == "None":
            self.setvar("HWID1", hwid)
            wid1 = hwid
        if wid2 == "None" and (wid1 != hwid):
            self.setvar("HWID2", hwid)
            wid2 = hwid

        if BREZILIAN:
            if wid1 != hwid:
                if self.page is not None:
                    self.log(f"user :{user} tried connecting on {public_ip}")
                    self.page.open_banner(
                        "Hardware id doesn't match, contact the admin"
                    )
                print("Hardware id doesn't match")
                return False
        else:
            if (wid1 != hwid) and (wid2 != hwid):
                if self.page is not None:
                    self.log(f"user :{user} tried connecting on {public_ip}")
                    self.page.open_banner(
                        "Hardware id doesn't match, contact the admin"
                    )
                print("Hardware id doesn't match")
                return False

        if json["success"]:
            self.__load_user_data(json["info"])
            return True
        else:
            if self.page is not None:
                if not BREZILIAN:
                    content = ft.Column(
                        controls=[
                            ft.TextButton(
                                icon=ft.icons.LINK_OUTLINED,
                                text="Pay with Stripe",
                                on_click=lambda _: self.page.launch_url(
                                    LinkSingleton().getStripeLink()
                                ),
                            ),
                            ft.TextButton(
                                icon=ft.icons.LINK_OUTLINED,
                                text="Pay with Crypto",
                                on_click=lambda _: self.page.launch_url(
                                    LinkSingleton().getSellixLink()
                                ),
                            ),
                        ]
                    )
                else:
                    content = ft.Column([ft.Text("Invalid credentials")])

                self.page.show_banner(
                    ft.Banner(
                        content=content,
                        actions=[
                            ft.TextButton(
                                "Close", on_click=lambda e: page.close_banner()
                            ),
                        ],
                        content_padding=ft.padding.all(5),
                    )
                )
            return False

    def license(self, key, hwid=None):
        self.checkinit()
        if hwid is None:
            hwid = others.get_hwid()

        post_data = {
            "type": "license",
            "key": key,
            "hwid": hwid,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid,
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            self.__load_user_data(json["info"])
        else:
            time.sleep(3)
            os._exit(1)

    def var(self, name):
        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()

        post_data = {
            "type": binascii.hexlify("var".encode()),
            "varid": encryption.encrypt(name, self.enckey, init_iv),
            "sessionid": binascii.hexlify(self.sessionid.encode()),
            "name": binascii.hexlify(self.name.encode()),
            "ownerid": binascii.hexlify(self.ownerid.encode()),
            "init_iv": init_iv,
        }

        response = self.__do_request(post_data)

        response = encryption.decrypt(response, self.enckey, init_iv)

        json = jsond.loads(response)

        if json["success"]:
            return json["message"]
        return "None"

    def getvar(self, var_name):
        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()

        post_data = {
            "type": binascii.hexlify("getvar".encode()),
            "var": encryption.encrypt(var_name, self.enckey, init_iv),
            "sessionid": binascii.hexlify(self.sessionid.encode()),
            "name": binascii.hexlify(self.name.encode()),
            "ownerid": binascii.hexlify(self.ownerid.encode()),
            "init_iv": init_iv,
        }
        response = self.__do_request(post_data)
        response = encryption.decrypt(response, self.enckey, init_iv)
        json = jsond.loads(response)

        if json["success"]:
            return json["response"]
        return "None"

    def setvar(self, var_name, var_data):
        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        post_data = {
            "type": binascii.hexlify("setvar".encode()),
            "var": encryption.encrypt(var_name, self.enckey, init_iv),
            "data": encryption.encrypt(var_data, self.enckey, init_iv),
            "sessionid": binascii.hexlify(self.sessionid.encode()),
            "name": binascii.hexlify(self.name.encode()),
            "ownerid": binascii.hexlify(self.ownerid.encode()),
            "init_iv": init_iv,
        }
        response = self.__do_request(post_data)
        response = encryption.decrypt(response, self.enckey, init_iv)
        json = jsond.loads(response)

        if json["success"]:
            return True
        else:
            print(json["message"])

    def webhook(self, webid, param, body="", conttype=""):
        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()

        post_data = {
            "type": binascii.hexlify("webhook".encode()),
            "webid": encryption.encrypt(webid, self.enckey, init_iv),
            "params": encryption.encrypt(param, self.enckey, init_iv),
            "body": encryption.encrypt(body, self.enckey, init_iv),
            "conttype": encryption.encrypt(conttype, self.enckey, init_iv),
            "sessionid": binascii.hexlify(self.sessionid.encode()),
            "name": binascii.hexlify(self.name.encode()),
            "ownerid": binascii.hexlify(self.ownerid.encode()),
            "init_iv": init_iv,
        }

        response = self.__do_request(post_data)

        response = encryption.decrypt(response, self.enckey, init_iv)
        json = jsond.loads(response)

        if json["success"]:
            return json["message"]
        else:
            print(json["message"])
            kill_app()

    def check(self):
        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()
        post_data = {
            "type": binascii.hexlify("check".encode()),
            "sessionid": binascii.hexlify(self.sessionid.encode()),
            "name": binascii.hexlify(self.name.encode()),
            "ownerid": binascii.hexlify(self.ownerid.encode()),
            "init_iv": init_iv,
        }
        try:
            response = self.__do_request(post_data)

            response = encryption.decrypt(response, self.enckey, init_iv)
            json = jsond.loads(response)
            if json["success"]:
                return True
            else:
                return False
        except:
            return False

    def log(self, message):
        if len(message) > 255:
            message = message[-255:]

        self.checkinit()
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()

        post_data = {
            "type": binascii.hexlify("log".encode()),
            "pcuser": encryption.encrypt(os.getenv("username"), self.enckey, init_iv),
            "message": encryption.encrypt(message, self.enckey, init_iv),
            "sessionid": binascii.hexlify(self.sessionid.encode()),
            "name": binascii.hexlify(self.name.encode()),
            "ownerid": binascii.hexlify(self.ownerid.encode()),
            "init_iv": init_iv,
        }

        self.__do_request(post_data)

    def fetchOnline(self):
        self.checkinit()
        print("test")
        init_iv = SHA256.new(str(uuid4())[:8].encode()).hexdigest()

        post_data = {
            "type": binascii.hexlify("fetchOnline".encode()),
            "sessionid": binascii.hexlify(self.sessionid.encode()),
            "name": binascii.hexlify(self.name.encode()),
            "ownerid": binascii.hexlify(self.ownerid.encode()),
            "init_iv": init_iv,
        }

        response = self.__do_request(post_data)
        response = encryption.decrypt(response, self.enckey, init_iv)

        json = jsond.loads(response)
        print(json)
        if json["success"]:
            if len(json["users"]) == 0:
                return None  # THIS IS ISSUE ON KEYAUTH SERVER SIDE 6.8.2022, so it will return none if it is not an array.
            else:
                return json["users"]
        else:
            return None

    def checkinit(self):
        if not self.initialized:
            print("Initialize first, in order to use the functions")
            kill_app()

    def __do_request(self, post_data, deadstop=0):
        try:
            rq_out = s.post("https://keyauth.win/api/1.0/", data=post_data, timeout=15)
            return rq_out.text
        except requests.exceptions.Timeout:
            if deadstop < 5:
                if self.page is not None:
                    self.page.pop_banner("Request timed out.. Please wait few minutes")
                print("Request timed out")
        except requests.exceptions.ConnectionError:
            if deadstop < 5:
                time.sleep(30)
                return self.__do_request(post_data, deadstop + 1)

    class application_data_c:
        numUsers = numKeys = app_ver = customer_panel = onlineUsers = ""

    # region user_data

    class user_data_c:
        username = (
            ip
        ) = hwid = expires = createdate = lastlogin = subscription = subscriptions = ""

    user_data = user_data_c()
    app_data = application_data_c()

    def __load_app_data(self, data):
        self.app_data.numUsers = data["numUsers"]
        self.app_data.numKeys = data["numKeys"]
        self.app_data.app_ver = data["version"]
        self.app_data.customer_panel = data["customerPanelLink"]
        self.app_data.onlineUsers = data["numOnlineUsers"]

    def __load_user_data(self, data):
        self.user_data.username = data["username"]
        self.user_data.ip = data["ip"]
        self.user_data.hwid = data["hwid"]
        self.user_data.expires = data["subscriptions"][0]["expiry"]
        self.user_data.createdate = data["createdate"]
        self.user_data.lastlogin = data["lastlogin"]
        self.user_data.subscription = data["subscriptions"][0]["subscription"]
        self.user_data.subscriptions = data["subscriptions"]


class others:
    @staticmethod
    def get_hwid():
        if platform.system() == "Linux":
            with open("/etc/machine-id") as f:
                hwid = f.read()
                return hwid
        elif platform.system() == "Windows":
            winuser = os.getlogin()
            sid = win32security.LookupAccountName(None, winuser)[
                0
            ]  # You can also use WMIC (better than SID, some users had problems with WMIC)
            hwid = win32security.ConvertSidToStringSid(sid)
            return hwid
        elif platform.system() == "Darwin":
            output = subprocess.Popen(
                "ioreg -l | grep IOPlatformSerialNumber",
                stdout=subprocess.PIPE,
                shell=True,
            ).communicate()[0]
            serial = output.decode().split("=", 1)[1].replace(" ", "")
            hwid = serial[1:-2]
            return hwid


class encryption:
    @staticmethod
    def encrypt_string(plain_text, key, iv):
        plain_text = pad(plain_text, 16)

        aes_instance = AES.new(key, AES.MODE_CBC, iv)

        raw_out = aes_instance.encrypt(plain_text)

        return binascii.hexlify(raw_out)

    @staticmethod
    def decrypt_string(cipher_text, key, iv):
        cipher_text = binascii.unhexlify(cipher_text)

        aes_instance = AES.new(key, AES.MODE_CBC, iv)

        cipher_text = aes_instance.decrypt(cipher_text)

        return unpad(cipher_text, 16)

    @staticmethod
    def encrypt(message, enc_key, iv):
        try:
            _key = SHA256.new(enc_key.encode()).hexdigest()[:32]

            _iv = SHA256.new(iv.encode()).hexdigest()[:16]

            return encryption.encrypt_string(
                message.encode(), _key.encode(), _iv.encode()
            ).decode()
        except:
            print(
                "Invalid Application Information. Long text is secret short text is ownerid. Name is supposed to be app name not username"
            )
            raise Exception

    @staticmethod
    def decrypt(message, enc_key, iv):
        try:
            _key = SHA256.new(enc_key.encode()).hexdigest()[:32]

            _iv = SHA256.new(iv.encode()).hexdigest()[:16]

            return encryption.decrypt_string(
                message.encode(), _key.encode(), _iv.encode()
            ).decode()
        except:
            print(
                "Invalid Application Information. Long text is secret short text is ownerid. Name is supposed to be app name not username"
            )
            raise Exception


class AuthSingleton:
    __instance = None
    FileLock = Lock()
    auth = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def setAuth(self, auth: selfApi) -> None:
        with self.FileLock:
            self.auth = auth

    def getAuth(self) -> selfApi:
        with self.FileLock:
            return self.auth
