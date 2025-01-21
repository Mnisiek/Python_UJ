"""Program realizuje podstawową wersję "gry w życie", korzystając z reguł
wymyślonych przez Johna Conwaya. Użytkownik ma możliwość wyboru początkowego
stanu komórek poprzez skorzystanie z kilku przykładowych układów albo
zaznaczenie całkowicie dowolnego własnego ułożenia komórek."""

import sys
import random
import pygame
from pygame.locals import MOUSEBUTTONDOWN, KEYDOWN, K_RETURN, K_q, K_SPACE

COLORS = {"black": (0, 0, 0), "gray": (128, 128, 128),
          "white": (255, 255, 255), "red": (255, 0, 0),
          "light gray": (80, 80, 80), "blue2": (63, 109, 140)}


class Life:
    """Główna klasa programu"""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = self.settings.clock
        self.size = (self.settings.width, self.settings.height)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Game of Life")
        self.grid = [[0 for _ in range(self.settings.cols)]
                     for _ in range(self.settings.rows)]

        self.buttons = [Button(self, "LOAD GRID 1", 34, (50, 20)),
                        Button(self, "LOAD GRID 2", 34, (50, 80)),
                        Button(self, "DRAW YOUR GRID", 34, (50, 140)),
                        Button(self, "RANDOM GRID", 34, (50, 200)),
                        Button(self, "START GAME", 34, (50, 260))]

    def run(self):
        """Działanie całego programu"""
        while True:
            self._check_events()

            if self.settings.game_running:
                self._update_cells()

            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_events(self):
        """Obsługa pętli zdarzeń"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == MOUSEBUTTONDOWN:
                self._handle_mouse(event.pos)
            elif event.type == KEYDOWN:
                self._handle_keydown_events(event.key)

    def _handle_mouse(self, pos):
        """Obsługa kliknięcia myszką"""
        for button in self.buttons:
            if button.rect.collidepoint(pos):
                self._handle_button_click(button.text)
                return

        # jeśli w trybie rysowania, zmień stan komórki na przeciwny
        if self.settings.drawing_mode:
            cell_size = self.settings.cell_size
            col, row = pos[0] // cell_size, pos[1] // cell_size
            if 0 <= row < self.settings.rows and 0 <= col < self.settings.cols:
                self.grid[row][col] = 1 - self.grid[row][col]

    def _handle_keydown_events(self, key):
        """Obsługa naciśnięcia klawiszy"""
        if key == K_q:
            pygame.quit()
            sys.exit(0)
        elif key == K_RETURN and self.settings.drawing_mode:
            self.settings.drawing_mode = False
        elif key == K_RETURN and not self.settings.drawing_mode:
            self.settings.game_running = True
        elif key == K_SPACE and self.settings.game_running:
            self.settings.game_running = False
            self.settings.drawing_mode = True
        elif key == K_SPACE and not self.settings.game_running:
            self.settings.drawing_mode = False
            self.settings.game_running = True

    def _handle_button_click(self, button_text):
        """Obsługa kliknięcia przycisku"""
        if not self.settings.game_running and not self.settings.drawing_mode:
            if button_text == "LOAD GRID 1":
                self._load_pattern("grid1.txt")
            elif button_text == "LOAD GRID 2":
                self._load_pattern("grid2.txt")
            elif button_text == "DRAW YOUR GRID":
                self.settings.drawing_mode = True
                self.grid = [[0 for _ in range(self.settings.cols)]
                             for _ in range(self.settings.rows)]
            elif button_text == "RANDOM GRID":
                self._generate_random_grid(self.settings.density)
                self.drawing_mode = False
                self.settings.game_running = False
            elif button_text == "START GAME":
                self.settings.drawing_mode = False
                self.settings.game_running = True

    def _load_pattern(self, filename):
        """Wczytanie wzoru z pliku"""
        try:
            with open(filename, "r") as f:
                for row_index, line in enumerate(f.readlines()):
                    line = line.split()
                    for col_index, value in enumerate(line):
                        if row_index < self.settings.rows and \
                                col_index < self.settings.cols:
                            self.grid[row_index][col_index] = int(value)
        except FileNotFoundError:
            print(f"Nie znaleziono pliku: {filename}")

    def _generate_random_grid(self, density):
        """Tworzenie losowej siatki komórek"""
        for row in range(self.settings.rows):
            for col in range(self.settings.cols):
                if random.random() < density:
                    self.grid[row][col] = 1
                else:
                    self.grid[row][col] = 0

    def _update_cells(self):
        """Obliczanie nowego stanu komórek"""
        # korzystamy ze zmiennej tymczasowej new_grid do zapisania
        # nowego ułożenia żywych komórek
        new_grid = [[0 for _ in range(self.settings.cols)] for _ in range(self.settings.rows)]
        for row_index, line in enumerate(self.grid):
            for col_index, value in enumerate(line):
                neighbors = self._count_neighbors(row_index, col_index)
                if not value and neighbors == 3:
                    new_grid[row_index][col_index] = 1
                elif value and (neighbors == 2 or neighbors == 3):
                    new_grid[row_index][col_index] = 1

        self.grid = new_grid

    def _count_neighbors(self, x, y):
        """Zliczanie sąsiadów"""
        neighbors = 0
        directions = ((-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1))
        for dx, dy in directions:
            x_pos = x + dx
            y_pos = y + dy
            if 0 <= x_pos < self.settings.rows and 0 <= y_pos < self.settings.cols:
                neighbors += self.grid[x_pos][y_pos]
        return neighbors

    def _update_screen(self):
        """Aktualizowanie zawartości wyświetlanej na ekranie"""
        self.screen.fill(COLORS.get("black"))
        self._draw_grid()
        if not self.settings.drawing_mode and not self.settings.game_running:
            for button in self.buttons:
                button.draw_button()
        pygame.display.flip()

    def _draw_grid(self):
        """Rysowanie siatki gry"""
        cell_size = self.settings.cell_size
        for row in range(self.settings.rows):
            for col in range(self.settings.cols):
                if self.grid[row][col]:
                    color = COLORS.get("white")
                else:
                    color = COLORS.get("black")
                pygame.draw.rect(self.screen, color, pygame.Rect(col * cell_size,
                    row * cell_size, cell_size - 1, cell_size - 1))


class Settings:
    """Klasa definiująca ustawienia programu"""

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.width = 800
        self.height = 600
        self.FPS = 5
        self.drawing_mode = False
        self.game_running = False

        self.cell_size = 10
        self.rows = self.height // self.cell_size
        self.cols = self.width // self.cell_size
        self.density = 0.25


class Button:
    """Klasa tworząca przycisk"""

    def __init__(self, game, text, font_size, position):
        self.screen = game.screen
        self.text = text
        self.width, self.height = (220, 50)
        self.button_color = COLORS.get("blue2")
        self.text_color = COLORS.get("white")
        self.font = pygame.font.SysFont(None, font_size)

        self.rect = pygame.Rect(position[0], position[1], self.width, self.height)
        self._prep_text(text)

    def _prep_text(self, msg):
        """Umieszczenie komunikatu w wygenerowanym obrazie"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Wyświetlenie przycisku z komunikatem"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


if __name__ == '__main__':
    gameOfLife = Life()
    gameOfLife.run()