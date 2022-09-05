from random import randint
import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self,main):
        super().__init__()
        self.main = main
        self.screen = main.screen
        self.image = pygame.image.load('car2.png')
        self.rect = self.image.get_rect()
        self.rect.x = randint(68,440)
        self.y = -100
    
    def update(self):
        if self.main.timer > 1200:
            self.screen.blit(self.image,(self.rect.x,self.y))
            self.y += 1.3
            self.rect.y = self.y
