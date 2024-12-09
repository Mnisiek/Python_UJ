
class Settings:
    """Klasa przeznaczona do przechowywania wszystkich ustawień gry"""

    def __init__(self):
        """Inicjalizacja ustawień gry"""
        self.screen_width = 1200
        self.screen_height = 800
        self.ship_limit = 3
        self.bg_color = (230, 230, 230)

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.fleet_drop_speed = 25
        self.speedup_scale = 1.5
#
        self.difficulty_button_y = 600
        self.easy_button_x = 20
#
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Inicjalizacja ustawień, które ulegają zmianie w trakcie gry"""
        self.ship_speed = 0.6
        self.bullet_speed = 1.0
        self.alien_speed = 0.1
        self.fleet_direction = 1

    def increase_speed(self):
        """Zmiana ustawień dotyczących szybkości"""
        #self.ship_speed *= self.speedup_scale
        #self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
