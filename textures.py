import arcade
from consts import *


class Textures:
    @staticmethod
    def textures_main_menu():
        Textures.textures_in_menu = {
            'bg': arcade.load_texture('main_menu_pic.png'),
            'name': arcade.load_texture('name_pic.png')
        }

    @staticmethod
    def set_fonts():
        Textures.fonts = {
            'pixel_sans': arcade.load_font('Comic Sans MS Pixel.ttf'),
        }

    @staticmethod
    def textures_pause():
        Textures.textures_in_pause = {

        }

    @staticmethod
    def textures_test_1():
        Textures.textures_in_game = {
            'Hero': arcade.load_texture('1.png'),
        }

        Textures.map_test_1 = "Test1.tmx"
        Textures.tile_map_test_1 = arcade.load_tilemap(Textures.map_test_1, scaling=3 * SCALE)

    @staticmethod
    def textures_test_2():
        hero = {'to_us': arcade.load_texture('Hero/Engineer.png'), 'walk': [],
                'in_air': arcade.load_texture('Hero/Engineer_Walk_4.png')}
        for i in range(1, 5):
            hero['walk'].append(arcade.load_texture(f"Hero/Engineer_Walk_{i}.png"))
        Textures.textures_in_game = {
            'Hero': hero,
        }

        Textures.map_test_2 = "Test2.tmx"
        Textures.tile_map_test_2 = arcade.load_tilemap(Textures.map_test_2, scaling=3 * SCALE)
