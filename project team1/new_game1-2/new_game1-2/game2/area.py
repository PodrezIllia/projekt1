import pygame
import os
import settings as settings
win_height = 800
win_width = 800

world_w = 100
world_h = 60

list_world_1 = [
    "01000000000",
    "11110000000",
    "01000111111",
    "01000001000",
    "01001101000",
    "01000001000",
    "01100001000",
    "01001001000",
    "01000001000", #
    "01000011000",
    "01001000000",
    "01000000000",
    "11111111111",
    "11111111111"
]
list_world_2 = [
    "0000000000",
    "0000000000",
    "1110000111",
    "0000010000",
    "1111000000",
    "0000000111",
    "0000100000",
    "0000001000",
    "0000000000",
    "0000010000",
    "0000100000",
    "0000000000",
    "1111111111",
    "1111111111"
]



# list_world_2 = [
    # "000000000",
    # "000000000",
    # "000000000",
    # "000000000",
    # "000000000",
    # "000000000",
    # "000000000",
    # "000101000", вот так наверное лучше
    # "000000000",
    # "000010000",
    # "000000000",
    # "000000000",
    # "111111111"
# ]
list_create_world = []
list_rect = []
class Area(settings.Settings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


def create_world(level):
    x = 0
    y = 0
    for string in level:
        for el in string:
            if el == "1":
                area = Area(
                    x= x,
                    y= y,
                    width= world_w,
                    height= world_h,
                    color= (255, 165, 0),
                    name_image= ("game2/images/test_image.png")
                )
                list_create_world.append(area)
                list_rect.append(area)
            x += world_w
        x = 0
        y += world_h

