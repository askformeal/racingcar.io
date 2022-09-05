import pygame

class Background:
    def __init__(self,main):
        self.screen = main.screen
        self.main = main
        self.image = pygame.image.load('back.bmp')
        self.y = -586
        
    def update(self):
        self.screen.blit(self.image,(0,self.y))
        self.y += 1
        if self.y >= 0:
            self.y = -586