import flet as ft

from views.tiles.tile import Tile


class TileHandler(ft.ListView):
    def __init__(self, page: ft.Page, **kwargs):
        super().__init__(**kwargs)
        self.initial_page = page
        self.expand = 0
        self.spacing = 5
        self.tiles: dict[str, Tile] = {}

    def add_tile(self, number: str):
        self.tiles[number] = Tile(self.initial_page, number)
        self.controls.append(self.tiles[number])
        self.initial_page.update()

    def unselect_all(self):
        for tile in self.controls[1:]:
            if isinstance(tile, Tile):
                tile.button_select.selected = False
        self.initial_page.update()

    def set_status(self, number: str, phrase: str):
        self.tiles[number].set_text(phrase)

    def refresh(self):
        instances = [("Nougat64", "main"), ("Nougat64_8", "second"), ('Nougat64_10', 'salutcgrefg5'), ('Nougat64_13', 'thereturnofthejedai'), ('Nougat64_22', 'atomtherobot'), ('Nougat64_9', 'sirefight2')]

        for instance in instances:
            if str(instance[0]) in self.tiles:
                self.controls.append(self.tiles[str(instance[0])])
                self.tiles[str(instance[0])].runner.adb.update_port()
                self.tiles[str(instance[0])].runner.adb.update_port()
            else:
                self.add_tile(str(instance[0]))

        self.initial_page.update()
