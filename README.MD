#but du projet: 

-Avoir un labyrinthe de taille k possédant une arrivée et une fin
-Une implémentation en arbre ou en graphe
-Une solution pour le labyrinthe créé
-Une interface pygame
-Un joueur doit pouvoir se déplacer dans le labirynthe



#solution possible:

-On créer un graphe avec une origine en haut à gauche
-Celui ci se déploie avec des directions aléatoires: gauche, droite, haut, bas
-Les images seront des chemins entre deux points du graphe avec la bonne orientation, le reste sera noir
-On répète l'opération du graphe jusqu'à ce que l'on est atteint une largeur et hauteur k
