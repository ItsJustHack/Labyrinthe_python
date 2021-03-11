from graphe import Sommet, Arc, Graphe
from random import choice, randint
from pile import Pile
import pygame
import time

def creer_damier_vide(k, addition=0):
    """
    entree: 
    -k:int, taille du damier
    -addition: int, coordonées addtionnées,
    exemple: Sommet(0,0) pour addition=0, Sommet(0.5,0.5) pour addition=0.5
    
    sortie: 
    -un dictionnaire composé de Sommet avec des coordonnées représentant une grille
    """
    return {
        (i + addition, j + addition): Sommet(
            (i + addition, j + addition), (i + addition, j + addition)
        )
        for i in range(k)
        for j in range(k)
    }


def creer_graphe(damier, k, addition=0):
    """
    entree:
    -damier: dict, damier créé grâce à 
    -k:int, taille du damier
    -addition: int, coordonées addtionnées (même que pour creer_damier_vide())

    sortie: 
    -graphe: renvoie un graphe reliant tout les sommets adjacents entre eux
    """
    graphe = Graphe()
    for y in range(k):
        for x in range(k):
            if x != k - 1 and y != k - 1: #on est pas sur les bords
                graphe.ajouterArc(
                    Arc(
                        (x + addition, y + addition),
                        damier[(x + addition, y + addition)],
                        damier[(x + 1 + addition, y + addition)],
                    )
                )
                graphe.ajouterArc(
                    Arc(
                        (x + addition, y + addition),
                        damier[(x + addition, y + addition)],
                        damier[(x + addition, y + 1 + addition)],
                    )
                )
            elif x == k - 1 and y != k - 1: #on est sur le bord droit
                graphe.ajouterArc(
                    Arc(
                        (x + addition, y + addition),
                        damier[(x + addition, y + addition)],
                        damier[(x + addition, y + 1 + addition)],
                    )
                )
            elif x != k - 1 and y == k - 1: #on est sur le bord bat
                graphe.ajouterArc(
                    Arc(
                        (x + addition, y + addition),
                        damier[(x + addition, y + addition)],
                        damier[(x + addition + 1, y + addition)],
                    )
                )
    return graphe


def creer_labirynthe(k, screen):
    """
    entree: 
    -k:int, taille du labirynthe
    
    sortie:
    -un graphe représentant un labyrinthe"""

    def affiche_ecran(graphe):
        screen.fill("black")
        for arc in graphe.arcs:
            x = (arc.s_origine.pos[0] * 600 / k, arc.s_origine.pos[1] * 600 /k)
            y = (arc.s_extremite.pos[0] * 600 / k, arc.s_extremite.pos[1] * 600 /k)
            pygame.draw.line(screen, "white", x, y, 1)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise "Jeu arrêté"


    damier = creer_damier_vide(k)
    damier_interne = creer_damier_vide(k - 1, 0.5)
    labirynthe = creer_graphe(damier, k)
    graphe_interne = creer_graphe(damier_interne, k - 1, 0.5)

    s_origine = graphe_interne.arcs[0].s_origine

    visite = []
    visite.append(s_origine)
    pile = Pile()
    pile.empiler(s_origine)

    creer_sortie(damier, labirynthe, k)

    while not pile.est_vide():
        sommet = pile.depiler()
        liste_sommets_adjacents_non_visites = list(
            set(graphe_interne.sommet_adjacent(sommet)) - set(visite)
        )
        if liste_sommets_adjacents_non_visites != []:
            pile.empiler(sommet)
            sommet_choisi = choice(liste_sommets_adjacents_non_visites)
            retire_arc(sommet.pos, sommet_choisi.pos, labirynthe, damier)
            visite.append(sommet_choisi)
            pile.empiler(sommet_choisi)
            affiche_ecran(labirynthe)

    return labirynthe


def direction(point_depart, point_arrivee):
    """renvoie la direction du parcours"""
    x = point_arrivee[0] - point_depart[0]
    y = point_arrivee[1] - point_depart[1]
    if x == 1.0:
        return "droite"
    if x == -1.0:
        return "gauche"
    if y == 1.0:
        return "bas"
    else:
        return "haut"



def creer_sortie(damier, graphe, k):
    p = randint(0, k - 2)
    graphe.retireArc(damier[(0, p)], damier[(0, p + 1)])
    graphe.retireArc(damier[(k - 1, k - p)], damier[(k - 1, k - p + 1)])


def retire_arc(sommet_origine, sommet_extremite, labirynthe, damier):
    """retire l'arc sur le graphe externe"""
    mouvement = direction(sommet_origine, sommet_extremite)
    x_depart = sommet_origine[0]
    y_depart = sommet_origine[1]
    x_arrivee = sommet_extremite[0]
    y_arrivee = sommet_extremite[1]

    if mouvement == "haut":
        labirynthe.retireArc(
            damier[x_depart - 0.5, y_depart - 0.5],
            damier[x_arrivee + 0.5, y_arrivee + 0.5],
        )
    elif mouvement == "bas":
        labirynthe.retireArc(
            damier[x_depart - 0.5, y_depart + 0.5],
            damier[x_arrivee + 0.5, y_arrivee - 0.5],
        )
    elif mouvement == "gauche":
        labirynthe.retireArc(
            damier[x_depart - 0.5, y_depart - 0.5],
            damier[x_arrivee + 0.5, y_arrivee + 0.5],
        )
    elif mouvement == "droite":
        labirynthe.retireArc(
            damier[x_depart + 0.5, y_depart - 0.5],
            damier[x_arrivee - 0.5, y_arrivee + 0.5],
        )

