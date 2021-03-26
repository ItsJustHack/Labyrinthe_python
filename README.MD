<h1 align="center">Labyrinthe pygame</h1>

### But du projet

- **Avoir un labyrinthe de taille k possédant une arrivée et une fin**

- **Une implémentation en arbre ou en graphe**

- **Une solution pour le labyrinthe créé**

- **Une interface pygame**

- **Un joueur doit pouvoir se déplacer dans le labirynthe**

### Génération du labirynthe

<p align="center"> <img src="./assets/labirynthe.png"> </p>

### Fonctionnement du labyrinthe

- **Deux graphes rectangulaires sont créés, un externe et un interne**

- **Le graphe interne se situe "à l'intérieur" du graphe externe**

- **On parcourt de façon aléatoire le graphe interne**

- **A chaque parcours entre deux sommets adjacents,**

- **L'arc "coupé" du graphe externe par le graphe interne est supprimé**

- **Ainsi on obtient le schéma suivant :**

<p align="center> ![](./assets/maze_generation.gif) </p>


