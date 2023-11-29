import flet as ft

from utils.Components.card import GenerateCard
from utils.flet_translations import translate
from views.settings.page_base import BasePage


class PageCharacter(BasePage):
    def __init__(self, profile):
        super().__init__(profile)

        self.add_control(
            GenerateCard(
                level="notice",
                subtitle=translate(
                    "Keep in mind that it will iterate on all of your favorite characters, it goes from top to bottom"
                ),
            ),
            ft.Switch(
                label=translate(
                    "Restart the game after switching\nto a new character (prevent freeze)"
                ),
                value=True
                if self.data[str(self.instance_index)]["schedules"][
                    str(self.profile_index)
                ]["leave_game_switch_character"]
                else False,
                on_change=lambda _: self.reverse_keyword("leave_game_switch_character"),
            ),
            # ft.Divider(),
            # ft.Text("Character Whitelist"),
        )

        # self.row_whitelist = ft.ResponsiveRow()
        # [self.row_whitelist.controls.append(ft.Checkbox(label=f"Profile {i}", col=4)) for i in range(9)]
        # self.add_control(self.row_whitelist)

    def reverse_keyword(self, keyword: str):
        super().reverse_keyword(keyword)
