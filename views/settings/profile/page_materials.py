from views.settings.page_base import BasePage
from views.settings.profile.rows.Flet_row_material import FletRowMaterial


class PageMaterials(BasePage):
    def __init__(self, profile):
        super().__init__(profile)

        keys = [
            "First",
            "Second",
            "Third",
            "Fourth",
            "Fifth",
        ]

        for i in range(1, 6):
            self.add_control(
                FletRowMaterial(
                    keys=keys,
                    i=i,
                    instance_index=self.instance_index,
                    profile_index=self.profile_index,
                )
            )
