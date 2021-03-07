from graphe import Sommet, Arc, Graphe
from random import choice, randint
from pile import Pile
import pygame
import time


taille = int(input("Combien de largeur ?"))


pygame.init()
screen = pygame.display.set_mode((900,900))
pygame.display.set_caption("Echecs")


def creer_damier_vide(k, addition=0):
    """créer un damier avec seulement des cases vides"""
    return {
        (i + addition, j + addition): Sommet(
            (i + addition, j + addition), (i + addition, j + addition)
        )
        for i in range(k)
        for j in range(k)
    }


def creer_graphe(damier, k, addition=0):
    """creer un graphe contenant des sommets"""
    graphe = Graphe()
    for y in range(k):
        for x in range(k):
            if x != k - 1 and y != k - 1:
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
            elif x == k - 1 and y != k - 1:
                graphe.ajouterArc(
                    Arc(
                        (x + addition, y + addition),
                        damier[(x + addition, y + addition)],
                        damier[(x + addition, y + 1 + addition)],
                    )
                )
            elif x != k - 1 and y == k - 1:
                graphe.ajouterArc(
                    Arc(
                        (x + addition, y + addition),
                        damier[(x + addition, y + addition)],
                        damier[(x + addition + 1, y + addition)],
                    )
                )
    return graphe


def creer_labirynthe(k):
    """renvoie un graphe de longueur et largeur k, contenant un labirynthe"""

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


def affiche_ecran(graphe):
    screen.fill("black")
    for arc in graphe.arcs:
        #x = (arc.s_origine.pos[0] * 6 * taille, arc.s_origine.pos[1] * 6 * taille)
        #y = (arc.s_extremite.pos[0] * 6 * taille, arc.s_extremite.pos[1] * 6 * taille)
        x = (arc.s_origine.pos[0] * 900 / taille, arc.s_origine.pos[1] * 900 /taille)
        y = (arc.s_extremite.pos[0] * 900 / taille, arc.s_extremite.pos[1] * 900 /taille)
        pygame.draw.line(screen, "white", x, y, 1)
    pygame.display.update()
    #time.sleep(0.3)


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


RUNNING = True
a = creer_labirynthe(taille)


while RUNNING:
    # mettre à jour l'écran
    for arc in a.arcs:
        #x = (arc.s_origine.pos[0] * 6 * taille, arc.s_origine.pos[1] * 6 * taille)
        #y = (arc.s_extremite.pos[0] * 6 * taille, arc.s_extremite.pos[1] * 6 * taille)
        x = (arc.s_origine.pos[0] * 2 /taille, arc.s_origine.pos[1] * 2 /taille)
        y = (arc.s_extremite.pos[0] * 2 /taille, arc.s_extremite.pos[1] * 2 /taille)
        pygame.draw.line(screen, "white", x, y, 1)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
