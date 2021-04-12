import random
import abstraction.probleme
from taquin.action import Action
from taquin.etat import Etat

class Probleme(abstraction.probleme.Probleme):
    """
    Classe représentant le problème du taquin comme :
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
        x, y = etat.position_vide
        for action in Action.actions_possibles():
            dx, dy = action.vecteur()
            if x+dx >= 0 and y+dy >= 0 and x+dx < etat.width and y+dy < etat.width:
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
