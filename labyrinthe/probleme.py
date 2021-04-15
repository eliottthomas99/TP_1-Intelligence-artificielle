import random
import abstraction.probleme
from labyrinthe.action import Action
from labyrinthe.etat import Etat

class Probleme(abstraction.probleme.Probleme):
    """
    Classe représentant le problème du labyrinthe comme :
    - un état initial
    - un prédicat but()
    - une méthode transition()
    """
    def __init__(self, etat_initial, etat_final):
        self.etat_initial = etat_initial
        self.etat_final = etat_final

    def get_etat_initial(self):
        """
        Renvoie l'état initial
        """
        return self.etat_initial

    def but(self, etat):
        """
        Renvoie vrai si l'état en paramètre est un état but
        """
        return etat == self.etat_final

    @classmethod
    def actions_possibles(cls, etat):
        """
        Renvoie la liste des actions possibles à partir d'un état donné
        """
        actions = []
        #print(etat.position_recherche)
        x, y = etat.position_recherche
        for action in Action.actions_possibles():
            dx, dy = action.vecteur()
            if x+dx >= 0 and y+dy >= 0 and x+dx < etat.width and y+dy < etat.width and (etat.plateau[x+dx][y+dy]) != 1:
                actions.append(action)
        return actions

    @classmethod
    def transition(cls, etat_courant, action):
        """
        Renvoie le nouvel état atteint à partir d'un état courant par une action donnée
        """
        return etat_courant.copier().deplacer(action.vecteur())

    @classmethod
    def cout(cls, etat_courant, action):
        """
        Renvoie le coût d'une action à partir d'un état donné
        """
        return 1

    def heuristique_manhattan(self, etat):
        """
        Une fonction d'heuristique qui calcule la somme des distances L1
        entre les positions actuelle et ciblée pour chaque tuille
        Cette heuristique est admissible.
        """
        x_values = [0]*((etat.width*etat.width)-1)
        y_values = [0]*((etat.width*etat.width)-1)
        for x in range(etat.width):
            for y in range(etat.width):
                # Mémoriser les positions actuelle et cible
                # Si pas la case vide
                if etat.plateau[x][y] != 0:
                    x_values[etat.plateau[x][y]-1] += x
                    y_values[etat.plateau[x][y]-1] += y
                if self.etat_final.plateau[x][y] != 0:
                    x_values[self.etat_final.plateau[x][y]-1] += -x
                    y_values[self.etat_final.plateau[x][y]-1] += -y
        return sum(map(abs, x_values))+sum(map(abs, y_values))


    def nombre_piece_mal_placees(self,etat):
        """
        Une fonction heuristique qui calcule le nombre de pièce mal placées

        """
        compteur = 0
        for i in range(len(etat.plateau)):
            for j in range(len(etat.plateau[0])):
                value = self.etat_final.plateau[i][j]
                if(etat.plateau[i][j] != value):
                    compteur+=1

        return compteur

    def heuristique_labyrinthe(self,etat):
        x_pos=0
        y_pos=0
        x_fin=0
        y_fin=0
        h=0
        for x in range (etat.width):
            for y in range(etat.width):
                if etat.plateau[x][y] == 3:
                    x_pos=x
                    y_pos=y
                if etat.plateau[x][y] == 2:
                    x_fin=x
                    y_fin=y
        h=ceil(math.sqrt(((x_fin-x_pos)**2)+((y_fin-y_pos)**2)))
        return h
