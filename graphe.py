class Sommet:
    def __init__(self,nom,pos):
        self.nom = nom
        self.pos = pos

    def __str__(self):
        return f"Sommet : {self.nom}"

class Arc:
    def __init__(self,nom,s_origine,s_extremite):
        self.nom=nom
        self.s_origine=s_origine
        self.s_extremite=s_extremite
    
    def __str__(self):
        return f"Arc {self.nom} de {self.s_origine.nom} à {self.s_extremite.nom}"


class Graphe:
    def __init__(self):
        self.arcs=[]
        self.compteur = 0
        self.appel = 0

    def ajouter_arc_inverse(self,arc):
        return Arc(arc.nom, arc.s_extremite, arc.s_origine)

    def ajouterArc(self,arc):
        self.arcs.append(arc)
        self.arcs.append(self.ajouter_arc_inverse(arc))
    
    def retireArc(self, s_origine, s_extremite):
        a = self.arcs.copy()
        for arc in a:
            if arc.s_origine == s_origine and arc.s_extremite == s_extremite:
                self.arcs.remove(arc)
            
            elif arc.s_extremite == s_origine and arc.s_origine == s_extremite:
                self.arcs.remove(arc)

    def sommet_adjacent(self, sommet):
        liste_sommets_adjacents = []
        for arc in self.arcs:
            if arc.s_origine == sommet:
                liste_sommets_adjacents.append(arc.s_extremite)
        return liste_sommets_adjacents

    def __str__(self):
        aff = ""
        aff += "\t Liste des arcs : \n"
        for a in self.arcs:
            aff += "\t\t"+str(a)+"\n"
        return aff
