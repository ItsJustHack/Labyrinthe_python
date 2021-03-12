from labyrinthe import creer_labirynthe
from player import Player
import pygame
import time

taille = int(input("Combien de largeur ?"))

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Echecs")

RUNNING = True
#while RUNNING:
labyrinthe = creer_labirynthe(taille, screen)
a, damier = labyrinthe[0], labyrinthe[1]


def affiche_ecran(graphe):
    screen.fill("black")
    for arc in graphe.arcs:
        x = (arc.s_origine.pos[0] * 600 / taille, arc.s_origine.pos[1] * 600 / taille)
        y = (arc.s_extremite.pos[0] * 600 / taille, arc.s_extremite.pos[1] * 600 / taille)
        pygame.draw.line(screen, "white", x, y, 1)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise "Jeu arrêté"

    #time.sleep(3)
player = Player(0.5,0.5,damier, a)

while RUNNING:

    screen.blit(player.image, ((player.x * 600 - 100) / taille, (player.y * 600 - 100) / taille))
    
    pygame.display.update()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            RUNNING = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                player.turn_right()
                time.sleep(0.1)
                affiche_ecran(a)

            if event.key == pygame.K_LEFT:
                player.turn_left()
                time.sleep(0.1)
                affiche_ecran(a)

            if event.key == pygame.K_UP:
                player.turn_up()
                time.sleep(0.1)
                affiche_ecran(a)

            if event.key == pygame.K_DOWN:
                player.turn_down()
                time.sleep(0.1)
                affiche_ecran(a)

