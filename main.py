from graphe import Sommet, Arc, Graphe
from random import choice, randint
from pile import Pile

#but du projet: 
"""
-Avoir un labyrinthe de taille k possédant une arrivée et une fin
-Une implémentation en arbre ou en graphe
-Une solution pour le labyrinthe créé
-Une interface pygame
-Un joueur doit pouvoir se déplacer dans le labirynthe
"""


#solution possible:
"""
-On créer un graphe avec une origine en haut à gauche
-Celui ci se déploie avec des directions aléatoires: gauche, droite, haut, bas
-Les images seront des chemins entre deux points du graphe avec la bonne orientation, le reste sera noir
-On répète l'opération du graphe jusqu'à ce que l'on est atteint une largeur et hauteur k
"""

def creer_damier_vide(k,addition=0):
        """créer un damier avec seulement des cases vides"""
        return {(i+addition,j+addition) : Sommet((i+addition,j+addition),(i+addition,j+addition)) for i in range(k) for j in range(k)}

def creer_graphe(damier, k, addition=0):
    """creer un graphe contenant des sommets"""
    graphe = Graphe()
    for y in range(k):
        for x in range(k):
            if x != k-1 and y != k-1:
                graphe.ajouterArc(Arc((x+addition,y+addition), damier[(x+addition,y+addition)], damier[(x+1+addition,y+addition)]))    
                graphe.ajouterArc(Arc((x+addition,y+addition), damier[(x+addition,y+addition)], damier[(x+addition,y+1+addition)]))
            elif x == k-1 and y != k-1:
                graphe.ajouterArc(Arc((x+addition,y+addition), damier[(x+addition,y+addition)], damier[(x+addition,y+1+addition)]))
            elif x != k-1 and y == k-1:
                graphe.ajouterArc(Arc((x+addition,y+addition), damier[(x+addition,y+addition)], damier[(x+addition+1,y+addition)])) 
    return graphe


def parcours_profondeur(graphe, s_origine):
    pile = Pile()
    sommet = s_origine
    visite = []
    resultat = []
    resultat.append(sommet.nom)
    visite.append(sommet)
    fin = False


    while True:
        
        liste_sommets_adjacents = graphe.sommet_adjacent(sommet)
        res = list(set(liste_sommets_adjacents)-set(visite))

        if res == []:
            while res == []:
                if not pile.est_vide():
                    sommet = pile.depiler()
                    liste_sommets_adjacents = graphe.sommet_adjacent(sommet)
                    res = list(set(liste_sommets_adjacents)-set(visite))
                else:
                    return resultat

        element = choice(res)
        
        if element in visite:
            if not pile.est_vide():
                sommet = pile.depiler()
            else:
                return resultat
        else:
            pile.empiler(sommet)
            sommet = element
            resultat.append(sommet.nom)
            visite.append(sommet)
    
def direction(point_depart, point_arrivee):
    """renvoie la direction du parcours"""
    x = point_arrivee[0]-point_depart[0]
    y = point_arrivee[1]-point_depart[1]
    if x == 1.0: return "droite"
    if x == -1.0: return "gauche"
    if y == 1.0: return "bas"
    else: return "haut"


def creer_labirynthe(k):

    damier = creer_damier_vide(k)
    damier_interne = creer_damier_vide(k-1, 0.5)
    labirynthe = creer_graphe(damier, k)
    graphe_interne = creer_graphe(damier_interne, k-1, 0.5)
    parcours_interne = parcours_profondeur(graphe_interne, damier_interne[(0.5,0.5)])
    print(len(parcours_interne))
    
    for i in range(len(parcours_interne)-1):
        mouvement = direction(parcours_interne[i], parcours_interne[i+1])
        x_depart = parcours_interne[i][0]
        y_depart = parcours_interne[i][1]
        x_arrivee = parcours_interne[i+1][0]
        y_arrivee = parcours_interne[i+1][1]


        if mouvement == "haut": 
            labirynthe.retireArc(damier[x_depart-0.5,y_depart-0.5],damier[x_arrivee+0.5, y_arrivee+0.5])
        elif mouvement == "bas":
            labirynthe.retireArc(damier[x_depart-0.5,y_depart+0.5],damier[x_arrivee+0.5, y_arrivee-0.5])
        elif mouvement == "gauche": 
            labirynthe.retireArc(damier[x_depart-0.5,y_depart-0.5],damier[x_arrivee+0.5, y_arrivee+0.5])
        elif mouvement == "droite": 
            labirynthe.retireArc(damier[x_depart+0.5,y_depart-0.5],damier[x_arrivee-0.5, y_arrivee+0.5])

    return labirynthe

#a = creer_graphe(creer_damier_vide(8), 8)
#print(a)
#damier = creer_damier_vide(7,0.5)
#graphe = creer_graphe(damier, 7, 0.5)
#b = creer_graphe(damier ,7)
#print(b)

#print(damier)


a = creer_labirynthe(7)
print(a.compteur)
print(a.appel)


    

