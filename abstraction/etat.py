class Etat:
    """
    Classe abstraite représentant un état
    """

    def copier(self):
        """
        Return a new puzzle with the same plateau as 'self'
        """
        raise NotImplementedError

    def afficher(self):
        raise NotImplementedError

    def __str__(self):
        """
        Transform l'état courant en une string
        """
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError
    
    def __eq__(self, obj):
        """
        Compare l'état courant à un autre
        """
        raise NotImplementedError

    def __hash__(self):
        return hash(str(self))
