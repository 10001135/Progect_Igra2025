import arcade
from camera_for_hero import CameraForHero
from textures import Textures
from hero import Hero
from consts import *
from pause_view import PauseView

class GameView_test_2(arcade.View):
    def __init__(self):
        super().__init__()
        Textures.textures_test_2()
        arcade.set_background_color(arcade.color.FRENCH_SKY_BLUE)

        self.walls_list = Textures.tile_map_test_2.sprite_lists['Walls']
        self.hero = Hero()
        self.hero.center_x = 200
        self.hero.center_y = 500
        self.hero_l = arcade.SpriteList()
        self.hero_l.append(self.hero)
        self.world_camera = CameraForHero(self.hero, Textures.tile_map_test_2)

        self.engine = arcade.PhysicsEnginePlatformer(
            player_sprite=self.hero,
            gravity_constant=GRAVITY,
            walls=self.walls_list,
        )
        self.hero.engine = self.engine


    def on_draw(self):
        self.clear()
        self.world_camera.use()
        self.walls_list.draw(pixelated=True)
        self.hero_l.draw(pixelated=True)

    def on_update(self, delta_time):
        for hero in self.hero_l:
            hero.on_update(delta_time)
            hero.update_animation(delta_time)
        self.world_camera.on_update()

    def on_key_press(self, key, modifiers):
        self.hero.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.hero.on_key_release(key, modifiers)
