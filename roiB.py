import pygame
from positionement import *

class RoiB(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/roiB.png')
        self.rect = self.image.get_rect()
        self.rect.x = 280
        self.rect.y = 428
        self.position = 0
        self.choi = False
        self.mouvement = []
        self.boufer = []

    def posMat(self):
        self.position = positions_roi(self.rect.x, self.rect.y)

    def move(self, echiquier):
        deplacement_rois(self.rect.x, self.rect.y, self.mouvement, echiquier, self.boufer)

    def moveUP(self):
        self.rect.y -= 50
    def moveDOWN(self):
        self.rect.y += 50
    def moveRIGHT(self):
        self.rect.x += 50
    def moveLEFT(self):
        self.rect.x -= 50