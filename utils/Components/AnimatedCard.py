from flet import *


class AnimatedCard(UserControl):
    def __init__(self, image_source_path, function):  # Corrected here
        super().__init__()
        self.image_source_path = image_source_path
        self.function = function

    def build(self):
        self._container = Container(
            width=220,
            height=300,
            bgcolor=colors.BLACK26,
            border_radius=12,
            on_hover=lambda e: self.AnimatedCardHover(e),
            on_click=self.function,
            data=self.image_source_path,
            animate=animation.Animation(600, "ease"),
            border=border.all(4, colors.WHITE24),
            content=Column(
                alignment="center",
                horizontal_alignment="start",
                spacing=0,
                controls=[
                    Image(
                        src=self.image_source_path,
                        fit=ImageFit.CONTAIN,
                    ),
                ],
            ),
        )

        self.__card = Card(
            elevation=0,
            content=Container(
                content=Column(
                    spacing=0,
                    horizontal_alignment="center",
                    controls=[
                        self._container,
                    ],
                ),
            ),
        )

        self._card = Column(
            horizontal_alignment="center",
            spacing=0,
            controls=[
                self.__card,
            ],
            col=6,
        )

        self._main = self._card

        return self._main

    def AnimatedCardHover(self, e):
        if e.data == "true":
            for __ in range(20):
                self.__card.elevation += 1
                self.__card.update()

            self._container.border = border.all(4, colors.BLUE_800)
            self._container.update()

        else:
            for __ in range(20):
                self.__card.elevation -= 1
                self.__card.update()

            self._container.border = border.all(4, colors.WHITE24)
            self._container.update()
