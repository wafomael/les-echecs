import pygame
from positionement import *


class CavaliersB(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/chevalB.png')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 435
        self.position = 0
        self.choi = False
        self.mouvement = []
        self.boufer = []

    def posMat(self):
        self.position = positions_pieces(self.rect.x, self.rect.y)

    def move(self, echiquier):
        deplacement_cavalier(self.rect.x, self.rect.y, self.mouvement, echiquier, self.boufer)

    def moveUP(self):
        self.rect.y -= 50
    def moveDOWN(self):
        self.rect.y += 50
    def moveRIGHT(self):
        self.rect.x += 50
    def moveLEFT(self):
        self.rect.x -= 50