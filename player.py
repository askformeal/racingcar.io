import pygame

class Player:
    def __init__(self,main):
        self.main = main
        self.screen = main.screen
        self.image = pygame.image.load('car1.png')
        self.rect = self.image.get_rect()
        self.y = 450
        self.rect.y = self.y
        self.x = 245

        self.move_left = False
        self.move_right = False

    def update(self):
        self.rect.x = self.x
        self.screen.blit(self.image,(self.x,self.y))
        if self.move_left:
            self.x -= 1
        elif self.move_right:
            self.x += 1

        if self.x < 68 or self.x > 440:
            #self.main.running = False
            if self.move_left:
                self.x += 1
            elif self.move_right:
                self.x -= 1