import pygame
from positionement import *


class PlayerB(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/player2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 74
        self.rect.y = 124
        self.position = 0

    def posMat(self):
        self.position = positions(self.rect.x, self.rect.y)

    def moveUP(self):
        self.rect.y -= 50
    def moveDOWN(self):
        self.rect.y += 50
    def moveRIGHT(self):
        self.rect.x += 50
    def moveLEFT(self):
        self.rect.x -= 50




