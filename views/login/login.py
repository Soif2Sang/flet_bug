import os
import sys
import threading
from datetime import datetime
from time import sleep

import flet as ft

from utils.auth import selfApi, update_user_info
from utils.constants import BREZILIAN
from utils.flet_translations import translate
from utils.functions import FileSingleton, getchecksum
from utils.singletons import ApiSingleton, LinkSingleton


def is_str_valid(username, password):
    for element in ["#", "$", "&", "|", "\0", "\n", "\r", "'", "'", '"', "\Z"]:
        if element in username or element in password:
            return False
    return True


class LoginUI(ft.Column):
    def __init__(self, page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initial_page = page
        self.fileSingleton = FileSingleton()
        self.data = self.fileSingleton.get_data()
        self.init()

    def show_payment_banner(self, e):
        self.initial_page.show_banner(
            ft.Banner(
                content=ft.Column(
                    controls=[
                        ft.TextButton(
                            icon=ft.icons.LINK_OUTLINED,
                            text="Pay with Stripe",
                            on_click=lambda _: self.initial_page.launch_url(
                                LinkSingleton().getStripeLink()
                            ),
                        ),
                        ft.TextButton(
                            icon=ft.icons.LINK_OUTLINED,
                            text="Pay with Crypto",
                            on_click=lambda _: self.initial_page.launch_url(
                                LinkSingleton().getSellixLink()
                            ),
                        ),
                    ]
                ),
                actions=[
                    ft.TextButton(
                        "Close", on_click=lambda e: self.initial_page.close_banner()
                    ),
                ],
                content_padding=ft.padding.all(5),
            )
        )

    def show_payment_banner(self, e):
        self.initial_page.show_bottom_sheet(
            ft.BottomSheet(
                content=ft.Row(
                    controls=[
                        ft.TextButton(
                            icon=ft.icons.LINK_OUTLINED,
                            text="Pay with Stripe",
                            on_click=lambda _: self.initial_page.launch_url(
                                LinkSingleton().getStripeLink()
                            ),
                        ),
                        ft.TextButton(
                            icon=ft.icons.LINK_OUTLINED,
                            text="Pay with Crypto",
                            on_click=lambda _: self.initial_page.launch_url(
                                LinkSingleton().getSellixLink()
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                open=True,
                dismissible=True,
                enable_drag=True,
                on_dismiss=lambda _: self.initial_page.close_bottom_sheet(),
            )
        )

    def login(self, e):
        try:
            self.initial_page.splash = ft.ProgressBar()
            self.button_login.disabled = True
            self.button_login.style = ft.ButtonStyle(
                color=ft.colors.GREY_300,
                side={
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.GREY_300),
                    ft.MaterialState.HOVERED: ft.BorderSide(1, ft.colors.GREY_300),
                },
                bgcolor=ft.colors.BLACK54,
            )
            self.initial_page.update()

            username = self.textfield_username.value
            password = self.textfield_password.value

            if username == "" or password == "":
                return
            if not is_str_valid(username, password):
                self.initial_page.open_banner("Illegal characters..")
                return
            if self.initial_page.keyauthapp.login(
                user=username, password=password, page=self.initial_page
            ):
                update_user_info(password, username)

                self.initial_page.splash = None
                self.button_login.disabled = False

                target_date = datetime.utcfromtimestamp(
                    int(self.initial_page.keyauthapp.user_data.expires)
                )

                current_date = datetime.utcnow()
                days = (target_date - current_date).days

                self.initial_page.title = f"RokNet - {days} Days left"
                self.initial_page.update()
                self.initial_page.go("/emulator-choice")

                ApiSingleton().setApiKey(self.initial_page.keyauthapp.var("2captcha"))

                self.initial_page.subscription_checker = threading.Thread(
                    target=self.verify_subscription, args=(username, password)
                )
                # self.initial_page.subscription_checker.start()
            else:
                sleep(5)
                self.initial_page.splash = None
                self.button_login.disabled = False
                self.button_login.style = ft.ButtonStyle(
                    color=ft.colors.GREY_300,
                    side={
                        ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.GREY_300),
                        ft.MaterialState.HOVERED: ft.BorderSide(1, ft.colors.GREY_300),
                    },
                )
                self.initial_page.update()
        except Exception as e:
            print(e)
            self.initial_page.window_close()
            os.system("taskkill /f /im flet.exe >nul 2>&1")
            sys.exit()

    def verify_subscription(self, username, password):
        try:
            self.initial_page.keyauthapp = selfApi(
                name="Rokbd" if not BREZILIAN else "RokbdBR",
                ownerid="7oofxdj8uH",
                secret="a968396e3fdfff2a2eaf14516fb283b7b7013e19cf392c863c90e0d8c41d9be0"
                if not BREZILIAN
                else "6d15b7ee5e7312238105efd4b648535835dc1ce5f4250fe2dc82910db43147b6",
                version="2.0",
                hash_to_check=getchecksum(),
            )

            if self.initial_page.keyauthapp.login(
                user=username, password=password, page=self.initial_page
            ):
                target_date = datetime.utcfromtimestamp(
                    int(self.initial_page.keyauthapp.user_data.expires)
                )

                current_date = datetime.utcnow()
                days_remaining = (target_date - current_date).days

                self.initial_page.title = f"RokNet - {days_remaining} Days left"
                self.initial_page.update()
                sleep(6 * 3600)
                return self.verify_subscription(username, password)
            else:
                for element in self.initial_page.tile_manager.tiles.values():
                    element.paused = False
                    element.stopped = True

                self.initial_page.go("/login")
        except Exception as e:
            print(e)
            self.initial_page.window_close()
            os.system("taskkill /f /im flet.exe >nul 2>&1")
            sys.exit()

    def init(self):
        self.textfield_username = ft.TextField(
            label=translate("Username"),
            width=300,
            value=self.data.get("user", {}).get("username", ""),
            color=ft.colors.GREY_300,
            border_color=ft.colors.GREY_300,
            cursor_color=ft.colors.GREY_300,
            label_style=ft.TextStyle(color=ft.colors.GREY_300),
        )
        self.textfield_password = ft.TextField(
            label=translate("Password"),
            color=ft.colors.GREY_300,
            border_color=ft.colors.GREY_300,
            cursor_color=ft.colors.GREY_300,
            label_style=ft.TextStyle(color=ft.colors.GREY_300),
            width=300,
            value=self.data.get("user", {}).get("password", ""),
            keyboard_type=ft.KeyboardType.VISIBLE_PASSWORD,
        )
        self.button_login = ft.OutlinedButton(
            text=translate("Login"),
            on_click=self.login,
            style=ft.ButtonStyle(
                color=ft.colors.GREY_300,
                side={
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.GREY_300),
                    ft.MaterialState.HOVERED: ft.BorderSide(1, ft.colors.GREY_600),
                },
            ),
        )
        self.subscribe_button = ft.OutlinedButton(
            text=translate("Subscribe"),
            on_click=self.show_payment_banner,
            style=ft.ButtonStyle(
                color=ft.colors.GREY_300,
                side={
                    ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.GREY_300),
                    ft.MaterialState.HOVERED: ft.BorderSide(1, ft.colors.GREY_600),
                },
            ),
        )

        r = ft.Row(
            controls=[
                ft.Column(controls=[self.button_login], col=4),
            ],
        )

        if not BREZILIAN:
            r.controls.append(ft.Column(controls=[self.subscribe_button], col=6))

        return self.controls.extend(
            [
                ft.Row(
                    [self.textfield_username], alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [self.textfield_password], alignment=ft.MainAxisAlignment.CENTER
                ),
                r,
            ]
        )
