# import itertools
# import random

import abstraction.etat

class Etat(abstraction.etat.Etat):
    """
    Classe représentant un état du labyrinthe comme un plateau et la position larrivee est 2 . 3 pour notre position
    Par exemple, [[0,0,0],[0,1,1],[0,4,3]], (2,1)
    """
    def __init__(self, plateau, position_recherche=None):
        self.width = len(plateau[0])
        self.plateau = plateau
        if position_recherche == None:
            self.position_recherche = tuple()
            for x in range(self.width):
                for y in range(self.width):
                    if self.plateau[x][y] == 3:
                        self.position_recherche = (x, y)
        else:
            self.position_recherche = position_recherche

    def copier(self):
        """
        Renvoie un clone de l'état courant
        """
        plateau = []
        for row in self.plateau:
            plateau.append([x for x in row])
        return Etat(plateau, self.position_recherche)

    def deplacer(self, deplacement):
        """
        Déplace une tuile par un certain déplacement, qu'il soit légal ou non
        """
        x, y = self.position_recherche
        dx, dy = deplacement
        # Échanger
        self.plateau[x][y], self.plateau[x+dx][y+dy] = self.plateau[x+dx][y+dy], self.plateau[x][y]
        self.position_recherche = (x+dx, y+dy)
        return self

    def afficher(self):
        for row in self.plateau:
            print(row)
        print()

    def __str__(self):
        return ''.join(map(str, self))

    def __iter__(self):
        for row in self.plateau:
            yield from row
    
    def __eq__(self, obj):
        return isinstance(obj, Etat) and obj.plateau == self.plateau

    def __hash__(self):
        return hash(str(self))
