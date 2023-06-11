import pygame
from positionement import *

class ReineB(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/reineB.png')
        self.rect = self.image.get_rect()
        self.rect.x = 230
        self.rect.y = 432
        self.position = 0
        self.choi = False
        self.mouvement = []
        self.boufer = []

    def posMat(self):
        self.position = positions_reine(self.rect.x, self.rect.y)

    def move(self, echiquier):
        deplacement_reinne(self.rect.x, self.rect.y, self.mouvement, echiquier, self.boufer)

    def moveUP(self):
        self.rect.y -= 50
    def moveDOWN(self):
        self.rect.y += 50
    def moveRIGHT(self):
        self.rect.x += 50
    def moveLEFT(self):
        self.rect.x -= 50