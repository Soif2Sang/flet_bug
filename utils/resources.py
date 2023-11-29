import os

from cv2 import imread

dir = "./resources"


class ImageSingleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.load_images()
        return cls.__instance

    def load_images(self):
        self.image_dict = {}
        for filename in os.listdir(dir):
            if filename.endswith(".png"):
                name = os.path.splitext(filename)[
                    0
                ]  # Extract the name without extension
                image = imread(os.path.join(dir, filename))
                self.image_dict[name] = image

        for filename in os.listdir(dir + "/buffs"):
            if filename.endswith(".png"):
                name = (
                    "buffs\\" + os.path.splitext(filename)[0]
                )  # Extract the name without extension
                image = imread(os.path.join(dir + "/buffs", filename))
                self.image_dict[name] = image

        for filename in os.listdir(dir + "/items"):
            if filename.endswith(".png"):
                name = (
                    "items\\" + os.path.splitext(filename)[0]
                )  # Extract the name without extension
                image = imread(os.path.join(dir + "/items", filename))
                self.image_dict[name] = image

    def get_file_name(self, file_name):
        if file_name not in self.image_dict:
            print(f"{file_name} not found")
        return self.image_dict.get(file_name, imread(f"{dir}/{file_name}.png"))
