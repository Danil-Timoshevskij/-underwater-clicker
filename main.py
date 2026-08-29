import os
import sys

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy import Config
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.properties import NumericProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.core.audio import SoundLoader 

Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'borderless', '0')

Window.size = (400, 600)

Builder.load_file('clicker.kv')

class Target(ButtonBehavior, Image):
    hp = NumericProperty(100)
    max_hp = NumericProperty(100)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type("on_death")
        self.source = "img/lens.png"

    def on_press(self):
        if self.hp > 0:
            self.hp -= 1
            if self.hp <= 0:
                self.hp = 0
                self.dispatch("on_death")

    def on_death(self):
        pass

    def respawn(self, new_hp=10, new_image=None):
        self.max_hp = new_hp
        self.hp = new_hp
        if new_image:
            self.source = new_image

class MenuScreen(Screen):
    def go_game(self, instance=None):
        self.manager.current = 'game'

    def go_settings(self, instance=None):
        self.manager.current = 'settings'

    def exit_app(self, instance=None):
        App.get_running_app().stop()


class GameScreen(Screen):
    levels = [
        {"hp": 100, "image": "img/lens.png"},
        {"hp": 150, "image": "img/ALONSO.png"},     
        {"hp": 200, "image": "img/Lourens.png"},
        {"hp": 250, "image": "img/Edrian.png"},
        {"hp": 300, "image": "img/AMR_26.png"},
    ]
    current_level = NumericProperty(0)

    def level_complete(self):
        print(f"Перемога на рівні {self.current_level + 1}!")
        self.current_level += 1

        if self.current_level >= len(self.levels):
            print("Вітаємо! Ви пройшли всі рівні!")
            self.current_level = 0

        next_lvl = self.levels[self.current_level]
        self.ids.monster.respawn(new_hp=next_lvl["hp"], new_image=next_lvl["image"])

        app = App.get_running_app()
        if self.current_level == 1:
            app.play_bg_track(app.bg_music_lvl2)
        else:
            app.play_bg_track(app.bg_music_default)

    def go_menu(self, instance=None):
        self.manager.current = 'menu'


class SettingsScreen(Screen):
    def go_menu(self, instance=None):
        self.manager.current = 'menu'

    def account_reset(self, instance=None):
        print("Всі налаштування скинуті до початкових значень.")
        game_screen = self.manager.get_screen('game')
        game_screen.current_level = 0
        first_lvl = game_screen.levels[0]
        game_screen.ids.monster.respawn(new_hp=first_lvl["hp"], new_image=first_lvl["image"])

        app = App.get_running_app()
        app.play_bg_track(app.bg_music_default)


class ClickerApp(App):
    title = "Aston Martin Aramco Formula One Team"
    icon = "img/AMR_26.png"

    def build(self):
        sm = ScreenManager(transition=RiseInTransition())
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(SettingsScreen(name='settings'))

        self.bg_music_default = SoundLoader.load('audio/f1_the_movie.mp3')
        self.bg_music_lvl2 = SoundLoader.load('audio/Alonso.mp3') 
        self.click_sound = SoundLoader.load('audio/click.mp3')
        self.win_sound = SoundLoader.load('assets/audio/win.mp3')
        self.current_bg = None
        self.play_bg_track(self.bg_music_default)

        return sm

    def play_bg_track(self, target_sound):
        if self.current_bg == target_sound and self.current_bg and self.current_bg.state == 'play':
            return

        if self.current_bg:
            self.current_bg.stop()
        self.current_bg = target_sound
        if self.current_bg:
            self.current_bg.loop = True
            self.current_bg.play()

    def play_click_sound(self):
        if self.click_sound:
            self.click_sound.seek(0) 
            self.click_sound.play()

    def toggle_music(self):
        if self.current_bg:
            if self.current_bg.state == 'play':
                self.current_bg.stop()
            else:
                self.current_bg.play()


if __name__ == '__main__':
    ClickerApp().run()