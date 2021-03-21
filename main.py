from labyrinthe import creer_labirynthe, affiche_ecran, affiche_sortie
from player import Player
from random import randint
from menu import Menu

import pygame
import time
import os

screen = pygame.display.set_mode((600, 600))  # définition des coordonnées de la fenêtre


def main(taille):

    pygame.init()  # initialisation de la fenêtre pygame

    RUNNING = True
    temp = creer_labirynthe(
        taille, screen
    )  # stockage dans une variable du résultat de la
    # fonction de création du labyrinthe
    labyrinthe, damier, solution = temp[0], temp[1], temp[2]  # stockage

    player = Player(damier, labyrinthe, taille)  # création du joueur

    while RUNNING:

        screen.blit(
            player.image,
            ((player.x * 600 - 100) / taille, (player.y * 600 - 100) / taille),
        )  # affichage du joueur

        for event in pygame.event.get():  # récupération des event

            if event.type == pygame.QUIT:  # fermeture de la fenêtre
                RUNNING = False

            if event.type == pygame.KEYDOWN:  # touche pressée

                if event.key == pygame.K_RIGHT:  # flêche droite
                    if player.turn_right() == 0:
                        print(
                            "Bien joué tu as terminé le labyrinthe, veux-tu recommencer ?"
                        )
                        RUNNING = False

                if event.key == pygame.K_LEFT:  # flêche gauche
                    player.turn_left()

                if event.key == pygame.K_UP:  # flêche haute
                    player.turn_up()

                if event.key == pygame.K_DOWN:  # flêche bas
                    player.turn_down()

                affiche_ecran(labyrinthe, taille, screen)

                if event.key == pygame.K_F1:  # touche F1: solution
                    affiche_sortie(solution, taille, screen)

        pygame.display.update()  # mise à jour de l'écran


if __name__ == "__main__":
    menu = Menu(main, screen)  # affichage du menu
