
import random

class Probleme:
    """
    Classe abstraite qui récapitule les méthodes nécessaire pour un probleme
    """
    
    def get_etat_initial(self):
        """
        Renvoie l'état initial
        """
        raise NotImplementedError
    
    def but(self, etat):
        """
        Renvoie vrai si l'état en paramètre est un état but
        """
        raise NotImplementedError

    @classmethod
    def actions_possibles(cls, etat):
        """
        Renvoie la liste des actions possibles à partir d'un état donné
        """
        raise NotImplementedError

    @classmethod
    def transition(cls, etat_courant, action):
        """
        Renvoie le nouvel état atteint à partir d'un état courant par une action donnée
        ATTENTION : l'état en entrée ne doit pas être modifier. Il faut en faire une copie.
        """
        raise NotImplementedError

    @classmethod
    def successeurs(cls, etat):
        """
        Renvoie les possibles états successeurs d'un état donné
        """
        for action in cls.actions_possibles(etat):
            yield cls.transition(etat, action)

    @classmethod
    def cout(etat_courant, action):
        """
        Renvoie le coût d'une action à partir d'un état donné
        """
        raise NotImplementedError

    @classmethod
    def melanger(cls, etat, n=100):
        """
        Retourne un etat mélangé
        """
        # Effectue n déplacements consécutifs aléatoires
        for _ in range(n):
            actions = cls.actions_possibles(etat)
            r = random.randint(0, len(actions)-1)
            etat = cls.transition(etat, actions[r])
        return etat


