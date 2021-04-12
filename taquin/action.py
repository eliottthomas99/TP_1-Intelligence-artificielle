import abstraction.action

class Action(abstraction.action.Action):
    """
    Classe représentant une action dans le jeu du taquin
    """

    # Static possible actions
    directions = {'Droite':( 0,-1),
                  'Gauche':( 0, 1),
                  'Bas':   ( 1, 0),
                  'Haut':  (-1, 0)}
        
    @classmethod
    def actions_possibles(cls):
        """
        Renvoie la liste de toutes les actions possibles
        """
        return map(lambda k: Action(k), Action.directions.keys())

    def __init__(self, direction):
        self.direction = direction

    def vecteur(self):
        """
        Renvoie le vecteur de déplacement associé à l'action
        """
        return Action.directions[self.direction]
    

    def legal(self, probleme):
        """
        indique si l'action est valable
        """

        

        




    def __str__(self):
        return self.direction

