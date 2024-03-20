import pygame
import sys
from settings import Settings
from ship import Ship

class Alien_Invasion:
    """Загальний клас для управління грою"""

    def __init__(self):
        """Ініціалізує гру та створює ігрові ресурси"""

        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.bg_color = self.settings.screen_color
        pygame.display.set_caption(self.settings.screen_caption)

        self.ship = Ship(self)


    def run_game(self):
        """Розпочинає головний цикл гри""" 

        while True:
            self._check_events()
            self._update_screen()
            pygame.display.flip()

    
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        #Move the ship to the right
                        self.ship.moving_right = True
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                    if event.key == pygame.K_UP:
                        self.ship.moving_up = True
                    if event.key == pygame.K_DOWN:
                        self.ship.moving_down = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        #Move the ship to the right
                        self.ship.moving_right = False
                    if event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                    if event.key == pygame.K_UP:
                        self.ship.moving_up = False
                    if event.key == pygame.K_DOWN:
                        self.ship.moving_down = False
                

    
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.update()
        self.ship.blitme()

if __name__ == '__main__':
    ai = Alien_Invasion()
    ai.run_game()