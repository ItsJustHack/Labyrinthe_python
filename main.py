from labyrinthe import creer_labirynthe, affiche_ecran, affiche_sortie
from player import Player
from random import randint
from menu import Menu

import pygame
import time
import os

screen = pygame.display.set_mode((600, 600))  # définition des coordonnées de la fenêtre


def main(taille,duo):
    pygame.init()  # initialisation de la fenêtre pygame

    RUNNING = True
    temp = creer_labirynthe(
        taille, screen
    )  # stockage dans une variable du résultat de la
    # fonction de création du labyrinthe
    labyrinthe, damier, solution = temp[0], temp[1], temp[2]  # stockage

    player1 = Player(damier, labyrinthe, taille,1)  # création du joueur
    if duo==True:
        player2 = Player(damier, labyrinthe, taille,2)


    while RUNNING:

        screen.blit(
            player1.image,
            ((player1.x * 600 - 100) / taille, (player1.y * 600 - 100) / taille),
        )  # affichage du joueur

        if duo:
            screen.blit(
                player2.image,
                ((player2.x * 600 - 100) / taille, (player2.y * 600 - 100) / taille),
        )


        for event in pygame.event.get():  # récupération des event

            if event.type == pygame.QUIT:  # fermeture de la fenêtre
                RUNNING = False

            if event.type == pygame.KEYDOWN:  # touche pressée

                if event.key == pygame.K_RIGHT:  # flêche droite
                    if player1.turn_right() == 0:
                        print(
                            "Bien joué tu as terminé le labyrinthe, veux-tu recommencer ?"
                        )
                        RUNNING = False

                if event.key == pygame.K_LEFT:  # flêche gauche
                    player1.turn_left()

                if event.key == pygame.K_UP:  # flêche haute
                    player1.turn_up()

                if event.key == pygame.K_DOWN:  # flêche bas
                    player1.turn_down()

                if duo:

                    if event.key == pygame.K_d:  #  droite
                        if player2.turn_right() == 0:
                            print(
                                "Bien joué tu as terminé le labyrinthe, veux-tu recommencer ?"
                            )
                            RUNNING = False

                    if event.key == pygame.K_q:  #  gauche
                        player2.turn_left()

                    if event.key == pygame.K_z:  #  haut
                        player2.turn_up()

                    if event.key == pygame.K_s:  #  bas
                        player2.turn_down()



                affiche_ecran(labyrinthe, taille, screen)

                if event.key == pygame.K_F1:  # touche F1: solution
                    affiche_sortie(solution, taille, screen)

        pygame.display.update()  # mise à jour de l'écran


if __name__ == "__main__":
    menu = Menu(main, screen)  # affichage du menu
