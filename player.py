from graphe import *
import pygame


class Player:
    def __init__(self, damier, graphe, taille, nombre):
        self.x = 0.5
        self.y = 0.5
        self.damier = damier
        self.graphe = graphe
        if nombre==1:
            self.i = pygame.image.load("assets/player.png")
        if nombre==2:
            self.i = pygame.image.load("assets/player2.png")
        self.image = pygame.transform.scale(self.i, (300 // taille, 300 // taille))

    def turn_right(self):  # fonction pour aller à droite
        if not self.graphe.presence_arc(
            self.damier[(self.x + 0.5, self.y + 0.5)],
            self.damier[(self.x + 0.5, self.y - 0.5)],
        ):
            try:
                self.x += 1
                self.damier[(self.x + 0.5, self.y + 0.5)]
            except KeyError:  # si on obtient une KeyError cela signifie que nous sommes en dehors du labyrinthe donc à la sortie
                return 0

    def turn_left(self):  # fonction pour aller à gauche
        if not self.graphe.presence_arc(
            self.damier[(self.x - 0.5, self.y + 0.5)],
            self.damier[(self.x - 0.5, self.y - 0.5)],
        ):
            self.x -= 1

    def turn_up(self):  # fonction pour monter
        if not self.graphe.presence_arc(
            self.damier[(self.x - 0.5, self.y - 0.5)],
            self.damier[(self.x + 0.5, self.y - 0.5)],
        ):
            self.y -= 1

    def turn_down(self):  # fonction pour descendre
        if not self.graphe.presence_arc(
            self.damier[(self.x - 0.5, self.y + 0.5)],
            self.damier[(self.x + 0.5, self.y + 0.5)],
        ):
            self.y += 1
