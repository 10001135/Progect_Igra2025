import arcade
from textures import Textures
from consts import *
from pause_view import PauseView


class GameView_test_1(arcade.View):
    def __init__(self):
        super().__init__()
        Textures.textures_test_1()
        arcade.set_background_color(arcade.color.FRENCH_SKY_BLUE)

        self.walls_list = Textures.tile_map_test_1.sprite_lists['Walls']
        self.enter_list = Textures.tile_map_test_1.sprite_lists['Enter']

    def on_draw(self):
        self.clear()
        self.walls_list.draw()
        self.enter_list.draw()

