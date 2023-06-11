from game import *
from positionement import *

pygame.init()

pygame.display.set_caption("Echec")
screen = pygame.display.set_mode((550, 550))

fond = pygame.image.load('assets/map.jpg')


game = Game()
activation = True

positionP = 90
positionT = 90
positionC = 140
positionF = 190
positionRE = 240
positionRO = 290

for pions in game.all_pions:
    pions.rect.x = positionP
    positionP += 50
for tours in game.all_tours:
    tours.rect.x = positionT
    positionT += 350
for cavalier in game.all_cavaliers:
    cavalier.rect.x = positionC
    positionC += 250
for fous in game.all_fous:
    fous.rect.x = positionF
    positionF += 150

positionP = 90
positionT = 90
positionC = 140
positionF = 190
positionRE = 240
positionRO = 290

for pions in game.all_pionsB:
    pions.rect.x = positionP
    positionP += 50
for tours in game.all_toursB:
    tours.rect.x = positionT
    positionT += 350
for cavalier in game.all_cavaliersB:
    cavalier.rect.x = positionC
    positionC += 250
for fous in game.all_fousB:
    fous.rect.x = positionF
    positionF += 150

select = True


def bouferP(posi):
    global select


    for pions in game.all_pionsB:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            piece.first = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True
    for pions in game.all_toursB:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            piece.first = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True
    for pions in game.all_fousB:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            piece.first = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True
    for pions in game.all_cavaliersB:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            piece.first = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True
    for pions in game.all_reineB:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            piece.choi = False
            piece.first = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True
    for pions in game.all_roisB:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            piece.first = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True

def bouferBP(posi):

    global select


    for pions in game.all_pions:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            piece.first = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True
    for pions in game.all_tours:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            piece.first = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True
    for pions in game.all_fous:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            piece.first = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True
    for pions in game.all_cavaliers:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            piece.first = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True
    for pions in game.all_reine:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            piece.choi = False
            piece.first = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True
    for pions in game.all_rois:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            piece.first = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True


def bouferB(posi):
    global select


    for pions in game.all_pions:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            piece.first = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True
    for pions in game.all_tours:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            piece.first = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True
    for pions in game.all_fous:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            piece.first = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True
    for pions in game.all_cavaliers:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            piece.first = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True
    for pions in game.all_reine:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            piece.choi = False
            piece.first = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True
    for pions in game.all_rois:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            piece.first = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True


def boufer(posi):

    global select

    for pions in game.all_pionsB:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True
    for pions in game.all_toursB:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True
    for pions in game.all_fousB:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True
    for pions in game.all_cavaliersB:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True
    for pions in game.all_reineB:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True
    for pions in game.all_roisB:
        if pions.position == posi:
            pions.kill()
            piece.choi = False
            for player in game.all_players:
                player.image = pygame.image.load("assets/player2.png")
                select = True





while activation:
    screen.blit(fond, (0, 0))

    game.all_players.draw(screen)
    game.all_pions.draw(screen)
    game.all_tours.draw(screen)
    game.all_cavaliers.draw(screen)
    game.all_fous.draw(screen)
    game.all_reine.draw(screen)
    game.all_rois.draw(screen)

    game.all_pionsB.draw(screen)
    game.all_toursB.draw(screen)
    game.all_cavaliersB.draw(screen)
    game.all_fousB.draw(screen)
    game.all_reineB.draw(screen)
    game.all_roisB.draw(screen)

    echiquier = []

    for player in game.all_players:
        player.posMat()
    for pions in game.all_pions:
        pions.posMat()
        echiquier.append(pions.position)
    for pions in game.all_tours:
        pions.posMat()
        echiquier.append(pions.position)
    for pions in game.all_cavaliers:
        pions.posMat()
        echiquier.append(pions.position)
    for pions in game.all_fous:
        pions.posMat()
        echiquier.append(pions.position)
    for pions in game.all_reine:
        pions.posMat()
        echiquier.append(pions.position)
    for pions in game.all_rois:
        pions.posMat()
        echiquier.append(pions.position)

    #BLANC
    for pions in game.all_pionsB:
        pions.posMat()
        echiquier.append(pions.position)
    for pions in game.all_toursB:
        pions.posMat()
        echiquier.append(pions.position)
    for pions in game.all_cavaliersB:
        pions.posMat()
        echiquier.append(pions.position)
    for pions in game.all_fousB:
        pions.posMat()
        echiquier.append(pions.position)
    for pions in game.all_reineB:
        pions.posMat()
        echiquier.append(pions.position)
    for pions in game.all_roisB:
        pions.posMat()
        echiquier.append(pions.position)



    #print(game.blanc.rect.x, game.blanc.rect.y)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            activation = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP and game.blanc.rect.y > 74:
            game.blanc.moveUP()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and game.blanc.rect.y < 424:
            game.blanc.moveDOWN()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and game.blanc.rect.x < 424:
            game.blanc.moveRIGHT()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and game.blanc.rect.x > 74:
            game.blanc.moveLEFT()


        if select:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                for player in game.all_players:
                    for piece in game.all_pions:
                        piece.choi = choix(player.rect.x, player.rect.y, piece.rect.x, piece.rect.y)
                        piece.move(echiquier)
                        #print(piece.mouvement)
                        #print(piece.choi)

                        if piece.choi:
                            select = False
                            player.image = pygame.image.load("assets/player1.png")
                        #print(echiquier)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                for player in game.all_players:
                    for piece in game.all_tours:
                        piece.choi = choix(player.rect.x, player.rect.y, piece.rect.x, piece.rect.y)
                        #print(piece.choi)
                        piece.move(echiquier)
                        if piece.choi:
                            select = False
                            player.image = pygame.image.load("assets/player1.png")


            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                for player in game.all_players:
                    for piece in game.all_cavaliers:
                        piece.choi = choix(player.rect.x, player.rect.y, piece.rect.x, piece.rect.y)
                        #print(piece.choi)
                        piece.move(echiquier)
                        if piece.choi:
                            select = False
                            player.image = pygame.image.load("assets/player1.png")

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                for player in game.all_players:
                    for piece in game.all_fous:
                        piece.choi = choix(player.rect.x, player.rect.y, piece.rect.x, piece.rect.y)
                        #print(piece.choi)
                        piece.move(echiquier)
                        if piece.choi:
                            select = False
                            player.image = pygame.image.load("assets/player1.png")

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                for player in game.all_players:
                    for piece in game.all_reine:
                        piece.choi = choix_reine(player.rect.x, player.rect.y, piece.rect.x, piece.rect.y)
                        #print(piece.choi)
                        piece.move(echiquier)
                        if piece.choi:
                            select = False
                            player.image = pygame.image.load("assets/player1.png")

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                for player in game.all_players:
                    for piece in game.all_rois:
                        piece.choi = choix_roi(player.rect.x, player.rect.y, piece.rect.x, piece.rect.y)
                        #print(piece.choi)
                        piece.move(echiquier)
                        if piece.choi:
                            select = False
                            player.image = pygame.image.load("assets/player1.png")

            #blanc
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                for player in game.all_players:
                    for piece in game.all_pionsB:
                        piece.choi = choix(player.rect.x, player.rect.y, piece.rect.x, piece.rect.y)
                        piece.move(echiquier)
                        #print(piece.choi)
                        if piece.choi:
                            select = False
                            player.image = pygame.image.load("assets/player1.png")

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                for player in game.all_players:
                    for piece in game.all_toursB:
                        piece.choi = choix(player.rect.x, player.rect.y, piece.rect.x, piece.rect.y)
                        #print(piece.choi)
                        piece.move(echiquier)
                        if piece.choi:
                            select = False
                            player.image = pygame.image.load("assets/player1.png")

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                for player in game.all_players:
                    for piece in game.all_cavaliersB:
                        piece.choi = choix(player.rect.x, player.rect.y, piece.rect.x, piece.rect.y)
                        #print(piece.choi)
                        piece.move(echiquier)
                        if piece.choi:
                            select = False
                            player.image = pygame.image.load("assets/player1.png")

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                for player in game.all_players:
                    for piece in game.all_fousB:
                        piece.choi = choix(player.rect.x, player.rect.y, piece.rect.x, piece.rect.y)
                        #print(piece.choi)
                        piece.move(echiquier)
                        if piece.choi:
                            select = False
                            player.image = pygame.image.load("assets/player1.png")

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                for player in game.all_players:
                    for piece in game.all_reineB:
                        piece.move(echiquier)
                        piece.choi = choix_reine(player.rect.x, player.rect.y, piece.rect.x, piece.rect.y)
                        #print(piece.choi)
                        if piece.choi:
                            select = False
                            player.image = pygame.image.load("assets/player1.png")

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                for player in game.all_players:
                    for piece in game.all_roisB:
                        piece.choi = choix_roi(player.rect.x, player.rect.y, piece.rect.x, piece.rect.y)
                        #print(piece.choi)
                        piece.move(echiquier)
                        if piece.choi:
                            select = False
                            player.image = pygame.image.load("assets/player1.png")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            for piece in game.all_pions:
                #print(piece.choi)
                if piece.choi and piece.rect.y < 424:
                    piece.moveDOWN()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            for piece in game.all_pions:
                #print(piece.choi)
                if piece.choi and piece.rect.y > 85:
                    piece.moveUP()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            for piece in game.all_pions:
                #print(piece.choi)
                if piece.choi and piece.rect.x < 435:
                    piece.moveRIGHT()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            for piece in game.all_pions:
                #print(piece.choi)
                if piece.choi and piece.rect.x > 90:
                    piece.moveLEFT()
                    #print("bouge")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            for piece in game.all_tours:
                #print(piece.choi)
                if piece.choi and piece.rect.y < 424:
                    piece.moveDOWN()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            for piece in game.all_tours:
                #print(piece.choi)
                if piece.choi and piece.rect.y > 85:
                    piece.moveUP()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            for piece in game.all_tours:
                #print(piece.choi)
                if piece.choi and piece.rect.x < 435:
                    piece.moveRIGHT()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            for piece in game.all_tours:
                #print(piece.choi)
                if piece.choi and piece.rect.x > 90:
                    piece.moveLEFT()
                    #print("bouge")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            for piece in game.all_cavaliers:
                #print(piece.choi)
                if piece.choi and piece.rect.y < 424:
                    piece.moveDOWN()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            for piece in game.all_cavaliers:
                #print(piece.choi)
                if piece.choi and piece.rect.y > 85:
                    piece.moveUP()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            for piece in game.all_cavaliers:
                #print(piece.choi)
                if piece.choi and piece.rect.x < 435:
                    piece.moveRIGHT()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            for piece in game.all_cavaliers:
                #print(piece.choi)
                if piece.choi and piece.rect.x > 90:
                    piece.moveLEFT()
                    #print("bouge")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            for piece in game.all_fous:
                #print(piece.choi)
                if piece.choi and piece.rect.y < 424:
                    piece.moveDOWN()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            for piece in game.all_fous:
                #print(piece.choi)
                if piece.choi and piece.rect.y > 85:
                    piece.moveUP()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            for piece in game.all_fous:
                #print(piece.choi)
                if piece.choi and piece.rect.x < 435:
                    piece.moveRIGHT()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            for piece in game.all_fous:
                #print(piece.choi)
                if piece.choi and piece.rect.x > 90:
                    piece.moveLEFT()
                    #print("bouge")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            for piece in game.all_reine:
                #print(piece.choi)
                if piece.choi and piece.rect.y < 424:
                    piece.moveDOWN()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            for piece in game.all_reine:
                #print(piece.choi)
                if piece.choi and piece.rect.y > 85:
                    piece.moveUP()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            for piece in game.all_reine:
                #print(piece.choi)
                if piece.choi and piece.rect.x < 435:
                    piece.moveRIGHT()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            for piece in game.all_reine:
                #print(piece.choi)
                if piece.choi and piece.rect.x > 90:
                    piece.moveLEFT()
                    #print("bouge")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            for piece in game.all_rois:
                #print(piece.choi)
                if piece.choi and piece.rect.y < 424:
                    piece.moveDOWN()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            for piece in game.all_rois:
                #print(piece.choi)
                if piece.choi and piece.rect.y > 85:
                    piece.moveUP()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            for piece in game.all_rois:
                #print(piece.choi)
                if piece.choi and piece.rect.x < 435:
                    piece.moveRIGHT()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            for piece in game.all_rois:
                #print(piece.choi)
                if piece.choi and piece.rect.x > 90:
                    piece.moveLEFT()
                    #print("bouge")


        #blanc
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            for piece in game.all_pionsB:
                #print(piece.choi)
                if piece.choi and piece.rect.y < 424:
                    piece.moveDOWN()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            for piece in game.all_pionsB:
                #print(piece.choi)
                if piece.choi and piece.rect.y > 85:
                    piece.moveUP()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            for piece in game.all_pionsB:
                #print(piece.choi)
                if piece.choi and piece.rect.x < 435:
                    piece.moveRIGHT()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            for piece in game.all_pionsB:
                #print(piece.choi)
                if piece.choi and piece.rect.x > 90:
                    piece.moveLEFT()
                    #print("bouge")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            for piece in game.all_toursB:
                #print(piece.choi)
                if piece.choi and piece.rect.y < 424:
                    piece.moveDOWN()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            for piece in game.all_toursB:
                #print(piece.choi)
                if piece.choi and piece.rect.y > 85:
                    piece.moveUP()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            for piece in game.all_toursB:
                #print(piece.choi)
                if piece.choi and piece.rect.x < 435:
                    piece.moveRIGHT()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            for piece in game.all_toursB:
                #print(piece.choi)
                if piece.choi and piece.rect.x > 90:
                    piece.moveLEFT()
                    #print("bouge")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            for piece in game.all_cavaliersB:
                #print(piece.choi)
                if piece.choi and piece.rect.y < 424:
                    piece.moveDOWN()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            for piece in game.all_cavaliersB:
                #print(piece.choi)
                if piece.choi and piece.rect.y > 85:
                    piece.moveUP()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            for piece in game.all_cavaliersB:
                #print(piece.choi)
                if piece.choi and piece.rect.x < 435:
                    piece.moveRIGHT()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            for piece in game.all_cavaliersB:
                #print(piece.choi)
                if piece.choi and piece.rect.x > 90:
                    piece.moveLEFT()
                    #print("bouge")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            for piece in game.all_fousB:
                #print(piece.choi)
                if piece.choi and piece.rect.y < 424:
                    piece.moveDOWN()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            for piece in game.all_fousB:
                #print(piece.choi)
                if piece.choi and piece.rect.y > 85:
                    piece.moveUP()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            for piece in game.all_fousB:
                #print(piece.choi)
                if piece.choi and piece.rect.x < 435:
                    piece.moveRIGHT()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            for piece in game.all_fousB:
                #print(piece.choi)
                if piece.choi and piece.rect.x > 90:
                    piece.moveLEFT()
                    #print("bouge")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            for piece in game.all_reineB:
                #print(piece.choi)
                if piece.choi and piece.rect.y < 424:
                    piece.moveDOWN()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            for piece in game.all_reineB:
                #print(piece.choi)
                if piece.choi and piece.rect.y > 85:
                    piece.moveUP()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            for piece in game.all_reineB:
                #print(piece.choi)
                if piece.choi and piece.rect.x < 435:
                    piece.moveRIGHT()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            for piece in game.all_reineB:
                #print(piece.choi)
                if piece.choi and piece.rect.x > 90:
                    piece.moveLEFT()
                    #print("bouge")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            for piece in game.all_roisB:
                #print(piece.choi)
                if piece.choi and piece.rect.y < 424:
                    piece.moveDOWN()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            for piece in game.all_roisB:
                #print(piece.choi)
                if piece.choi and piece.rect.y > 85:
                    piece.moveUP()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            for piece in game.all_roisB:
                #print(piece.choi)
                if piece.choi and piece.rect.x < 435:
                    piece.moveRIGHT()
                    #print("bouge")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            for piece in game.all_roisB:
                #print(piece.choi)
                if piece.choi and piece.rect.x > 90:
                    piece.moveLEFT()
                    #print("bouge")



        if event.type == pygame.KEYDOWN and event.key == pygame.K_x:

            for piece in game.all_pions:
                if piece.choi:
                    for i in range(len(piece.mouvement)):
                        if piece.mouvement[i] == piece.position and piece.choi:
                            piece.choi = False
                            piece.first = False
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/player2.png")
                                select = True
                        elif piece.mouvement[i] != piece.position and piece.choi:
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/erreur.png")
                            #print(piece.mouvement)

                    for i in range(len(piece.boufer)):
                        if piece.boufer[i] == piece.position:
                            bouferP(piece.position)
                piece.boufer = []




                if not piece.choi:
                    piece.mouvement = []


            for piece in game.all_tours:
                #print(piece.mouvement)
                if piece.choi:
                    for i in range(len(piece.mouvement)):
                        if piece.mouvement[i] == piece.position and piece.choi:
                            piece.choi = False
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/player2.png")
                            select = True
                        elif piece.mouvement[i] != piece.position and piece.choi:
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/erreur.png")
                            #print(piece.mouvement)

                    for i in range(len(piece.boufer)):
                        if piece.boufer[i] == piece.position:
                            #print(piece.boufer[i], piece.position)
                            boufer(piece.position)

                piece.boufer = []

                if not piece.choi:
                    piece.mouvement = []

            for piece in game.all_cavaliers:
                if piece.choi:
                    for i in range(len(piece.mouvement)):
                        if piece.mouvement[i] == piece.position and piece.choi:
                            piece.choi = False
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/player2.png")
                            select = True
                        elif piece.mouvement[i] != piece.position and piece.choi:
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/erreur.png")
                            # print(piece.mouvement)

                    for i in range(len(piece.boufer)):
                        if piece.boufer[i] == piece.position:
                            # print(piece.boufer)
                            boufer(piece.position)

                piece.boufer = []

                if not piece.choi:
                    piece.mouvement = []


            for piece in game.all_fous:
                if piece.choi:
                    for i in range(len(piece.mouvement)):
                        if piece.mouvement[i] == piece.position and piece.choi:
                            piece.choi = False
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/player2.png")
                            select = True
                        elif piece.mouvement[i] != piece.position and piece.choi:
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/erreur.png")
                            # print(piece.mouvement)

                    for i in range(len(piece.boufer)):
                        if piece.boufer[i] == piece.position:
                            #print(piece.boufer)
                            boufer(piece.position)

                piece.boufer = []

                if not piece.choi:
                    piece.mouvement = []


            for piece in game.all_reine:
                if piece.choi:
                    for i in range(len(piece.mouvement)):
                        if piece.mouvement[i] == piece.position and piece.choi:
                            piece.choi = False
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/player2.png")
                            select = True
                        elif piece.mouvement[i] != piece.position and piece.choi:
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/erreur.png")
                            # print(piece.mouvement)

                    for i in range(len(piece.boufer)):
                        if piece.boufer[i] == piece.position:

                            boufer(piece.position)

                piece.boufer = []


            for piece in game.all_rois:
                if piece.choi:
                    for i in range(len(piece.mouvement)):
                        if piece.mouvement[i] == piece.position and piece.choi:
                            piece.choi = False
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/player2.png")
                            select = True
                        elif piece.mouvement[i] != piece.position and piece.choi:
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/erreur.png")
                            # print(piece.mouvement)

                    for i in range(len(piece.boufer)):
                        if piece.boufer[i] == piece.position:
                            boufer(piece.position)

                piece.boufer = []

            for piece in game.all_pionsB:
                if piece.choi:
                    for i in range(len(piece.mouvement)):
                        if piece.mouvement[i] == piece.position and piece.choi:
                            piece.choi = False
                            piece.first = False
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/player2.png")
                                select = True
                        elif piece.mouvement[i] != piece.position and piece.choi:
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/erreur.png")
                            # print(piece.mouvement)

                    for i in range(len(piece.boufer)):
                        if piece.boufer[i] == piece.position:
                            bouferBP(piece.position)

                piece.boufer = []

                if not piece.choi:
                    piece.mouvement = []

            for piece in game.all_toursB:
                if piece.choi:
                    for i in range(len(piece.mouvement)):
                        if piece.mouvement[i] == piece.position and piece.choi:
                            piece.choi = False
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/player2.png")
                            select = True
                        elif piece.mouvement[i] != piece.position and piece.choi:
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/erreur.png")
                            # print(piece.mouvement)


                    for i in range(len(piece.boufer)):
                        if piece.boufer[i] == piece.position:
                            piece.choi = False
                            bouferB(piece.position)

                piece.boufer = []


                if not piece.choi:
                    piece.mouvement = []

            for piece in game.all_cavaliersB:
                if piece.choi:
                    for i in range(len(piece.mouvement)):
                        if piece.mouvement[i] == piece.position and piece.choi:
                            piece.choi = False
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/player2.png")
                            select = True
                        elif piece.mouvement[i] != piece.position and piece.choi:
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/erreur.png")
                            # print(piece.mouvement)

                    for i in range(len(piece.boufer)):
                        if piece.boufer[i] == piece.position:
                            piece.choi = False
                            bouferB(piece.position)

                piece.boufer = []

                if not piece.choi:
                    piece.mouvement = []


            for piece in game.all_fousB:
                if piece.choi:
                    for i in range(len(piece.mouvement)):
                        if piece.mouvement[i] == piece.position and piece.choi:
                            piece.choi = False
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/player2.png")
                            select = True
                        elif piece.mouvement[i] != piece.position and piece.choi:
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/erreur.png")
                            # print(piece.mouvement)

                    for i in range(len(piece.boufer)):
                        if piece.boufer[i] == piece.position:
                            piece.choi = False
                            bouferB(piece.position)

                piece.boufer = []

                if not piece.choi:
                    piece.mouvement = []


            for piece in game.all_reineB:
                if piece.choi:
                    for i in range(len(piece.mouvement)):
                        if piece.mouvement[i] == piece.position and piece.choi:
                            piece.choi = False
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/player2.png")
                            select = True
                        elif piece.mouvement[i] != piece.position and piece.choi:
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/erreur.png")
                            # print(piece.mouvement)

                    for i in range(len(piece.boufer)):
                        if piece.boufer[i] == piece.position:
                            bouferB(piece.position)

                piece.boufer = []

            for piece in game.all_roisB:
                if piece.choi:
                    for i in range(len(piece.mouvement)):
                        if piece.mouvement[i] == piece.position and piece.choi:
                            piece.choi = False
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/player2.png")
                            select = True
                        elif piece.mouvement[i] != piece.position and piece.choi:
                            for player in game.all_players:
                                player.image = pygame.image.load("assets/erreur.png")
                            # print(piece.mouvement)

                    for i in range(len(piece.boufer)):
                        if piece.boufer[i] == piece.position:
                            bouferB(piece.position)

                piece.boufer = []
