import pygame

class Ship:
    """Клас для управління кораблем"""

    def __init__(self, ai_game):
        """Ініціалізує(створює) корабель та задає його стартову позицію"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right == True:
            self.rect.x += 1
        if self.moving_left == True:
            self.rect.x -= 1
        if self.moving_up == True:
            self.rect.y -= 1
        if self.moving_down == True:
            self.rect.y +=1
    
    def blitme(self):
        """Малює корабель"""

        self.screen.blit(self.image, self.rect)