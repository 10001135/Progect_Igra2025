import arcade
from textures import Textures
from consts import *
from texts import text_d
from main_menu_view import MainMenuView
from game_view_test_1 import GameView_test_1
from game_view_test_2 import GameView_test_2


class Platformer(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, text_d['title'], antialiasing=True)
        self.set_fullscreen(False)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.F and (modifiers & arcade.key.LCTRL):
            self.set_fullscreen(not self.fullscreen)


def main():
    window = Platformer()
    Textures.set_fonts()
    main_menu_view = MainMenuView()
    window.show_view(main_menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
