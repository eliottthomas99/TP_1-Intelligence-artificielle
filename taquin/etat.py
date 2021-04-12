# import itertools
# import random

import abstraction.etat

class Etat(abstraction.etat.Etat):
    """
    Classe représentant un état du taquin comme un plateau et la position de la case vide
    Par exemple, [[1,2,3],[4,0,6],[7,5,8]], (1,1)
    """
    def __init__(self, plateau, position_vide=None):
        self.width = len(plateau[0])
        self.plateau = plateau
        if position_vide == None:
            self.position_vide = tuple()
            for x in range(self.width):
                for y in range(self.width):
                    if self.plateau[x][y] == 0:
                        self.position_vide = (x, y)
        else:
            self.position_vide = position_vide

    def copier(self):
        """
        Renvoie un clone de l'état courant
        """
        plateau = []
        for row in self.plateau:
            plateau.append([x for x in row])
        return Etat(plateau, self.position_vide)

    def deplacer(self, deplacement):
        """
        Déplace une tuile par un certain déplacement, qu'il soit légal ou non
        """
        x, y = self.position_vide
        dx, dy = deplacement
        # Échanger
        self.plateau[x][y], self.plateau[x+dx][y+dy] = self.plateau[x+dx][y+dy], self.plateau[x][y]
        self.position_vide = (x+dx, y+dy)
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
