import flet as ft

from utils.Components.card import GenerateCard
from utils.flet_translations import translate
from views.settings.page_base import BasePage
from views.settings.profile.rows.Flet_row_rss import FletRowRss


class PageRss(BasePage):
    def __init__(self, profile):
        super().__init__(profile)

        keys = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh"]

        self.add_control(
            GenerateCard(
                level=translate("tips"),
                subtitle=translate(
                    "If you plan on having the safest configuration, take a look at 'Zoom out method' and 'random' node choice!"
                ),
            ),
            ft.Switch(
                label=translate("Use Yellow presets as gatherers"),
                value=True
                if self.data[str(self.instance_index)]["schedules"][
                    str(self.profile_index)
                ]["rss_custom_preset"]
                else False,
                on_change=lambda _: self.reverse_keyword("rss_custom_preset"),
            ),
            ft.Switch(
                label=translate(
                    "Use zoom out method\n(the bot won't read node levels but is safer)"
                ),
                value=True
                if self.data[str(self.instance_index)]["schedules"][
                    str(self.profile_index)
                ]["gather_rss_method"]
                else False,
                on_change=lambda _: self.reverse_keyword("gather_rss_method"),
            ),
        )

        for key in keys:
            self.add_control(
                FletRowRss(
                    key=key,
                    instance_index=self.instance_index,
                    profile_index=self.profile_index,
                )
            )

    def reverse_keyword(self, keyword: str):
        super().reverse_keyword(keyword)

        self.data = self.FileSingleton.get_data()
        if keyword == "gather_rss_method":
            for control in self.profile.content.controls[-7:]:
                control.controls[2].controls[0].disabled = self.data[
                    str(self.instance_index)
                ]["schedules"][str(self.profile_index)]["gather_rss_method"]
        self.profile.initial_page.update()
