from labyrinthe import creer_labirynthe, affiche_ecran
from player import Player
from random import randint
import pygame
import time
import os


os.system("clear")
taille = int(input("Combien de largeur ?"))

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Labirynthe")

RUNNING = True
#while RUNNING:
labyrinthe = creer_labirynthe(taille, screen)
a, damier = labyrinthe[0], labyrinthe[1]


    #time.sleep(3)
player = Player(0.5, randint(0, taille - 1) + 0.5,damier, a)

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
                affiche_ecran(a, taille, screen)

            if event.key == pygame.K_LEFT:
                player.turn_left()
                time.sleep(0.1)
                affiche_ecran(a, taille, screen)

            if event.key == pygame.K_UP:
                player.turn_up()
                time.sleep(0.1)
                affiche_ecran(a, taille, screen)

            if event.key == pygame.K_DOWN:
                player.turn_down()
                time.sleep(0.1)
                affiche_ecran(a, taille, screen)

