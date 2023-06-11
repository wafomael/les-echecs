from blanc import *
from pions import *
from tours import *
from cavalier import *
from fous import *
from reine import *
from roi import *
from pionB import *
from tourB import *
from cavalierB import *
from fouB import *
from reineB import *
from roiB import *



class Game():
    def __init__(self):
        self.blanc = PlayerB()
        self.all_players = pygame.sprite.Group()
        self.blanc.add(self.all_players)
        self.all_pions = pygame.sprite.Group()
        self.all_tours = pygame.sprite.Group()
        self.all_cavaliers = pygame.sprite.Group()
        self.all_fous = pygame.sprite.Group()
        self.all_reine = pygame.sprite.Group()
        self.all_rois = pygame.sprite.Group()
        self.all_pionsB = pygame.sprite.Group()
        self.all_toursB = pygame.sprite.Group()
        self.all_cavaliersB = pygame.sprite.Group()
        self.all_fousB = pygame.sprite.Group()
        self.all_reineB = pygame.sprite.Group()
        self.all_roisB = pygame.sprite.Group()
        self.spawn(1)
        self.spawn(1)
        self.spawn(1)
        self.spawn(1)
        self.spawn(1)
        self.spawn(1)
        self.spawn(1)
        self.spawn(1)
        self.spawn(2)
        self.spawn(2)
        self.spawn(3)
        self.spawn(3)
        self.spawn(4)
        self.spawn(4)
        self.spawn(5)
        self.spawn(6)
        self.all_pices = pygame.sprite.Group()


    def spawn(self, p):
        if p == 1:
            self.all_pions.add(Pions())
            self.all_pionsB.add(PionsB())
        elif p == 2:
            self.all_tours.add(Tours())
            self.all_toursB.add(ToursB())
        elif p == 3:
            self.all_cavaliers.add(Cavaliers())
            self.all_cavaliersB.add(CavaliersB())
        elif p == 4:
            self.all_fous.add(Fous())
            self.all_fousB.add(FousB())
        elif p == 5:
            self.all_reine.add(Reine())
            self.all_reineB.add(ReineB())
        elif p == 6:
            self.all_rois.add(Roi())
            self.all_roisB.add(RoiB())

        #print(len(self.all_pions))

