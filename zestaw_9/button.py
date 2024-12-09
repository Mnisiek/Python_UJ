import pygame.font

class Button:
    """Klasa tworząca przycisk"""

    def __init__(self, ai_game, msg):
        """Inicjalizacja atrybutów przycisku"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (80, 80, 80)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """Umieszczenie komunikatu w wygenerowanym obrazie
        i wyśrodkowanie tekstu na przycisku"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Wyświetlenie przycisku z komunikatem"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

"""
class DifficultyButtons(Button):
    def __init__(self, ai_game, msg):
        super().__init__(ai_game, msg)
        self.button_color = (100, 100, 100)
        self.rect.left = 50
        self.rect.top = 600
        
        self._prep_msg(msg)
    
    def _create_difficulty_buttons(self):
        self.easy_button = DifficultyButtons(self, "Łatwy")
        self.easy_button.rect.x = self.settings.easy_button_x
        self.easy_button.rect.y = self.settings.difficulty_button_y
        self.medium_button = Button(self, "Średni")
        self.medium_button.rect.x = (3 * self.settings.easy_button_x
                                    + self.medium_button.width)
        self.medium_button.rect.y = self.settings.difficulty_button_y
        self.hard_button = Button(self, "Trudny")
        self.hard_button.rect.x = (5 * self.settings.easy_button_x
                                   + 2 * self.medium_button.width)
        self.hard_button.rect.y = self.settings.difficulty_button_y
"""