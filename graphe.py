class Sommet:
    def __init__(self,nom):
        self.nom = nom

    def __str__(self):
        return f"Sommet : {self.nom}"

class Arc:
    def __init__(self,nom,s_origine,s_extremite,direction):
        self.nom=nom
        self.s_origine=s_origine
        self.s_extremite=s_extremite
        self.direction = direction
    
    def __str__(self):
        return f"Arc {self.nom} de {self.s_origine.nom} à {self.s_extremite.nom}"


class Graphe:
    def __init__(self):
        self.arcs=[]

    def ajouterArc(self,arc):
        self.arcs.append(arc)

    def __str__(self):
        affiche = ""
        for arc in self.arcs:
            affiche += arc.direction
        return affiche
