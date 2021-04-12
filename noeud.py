
class Noeud:
    """
   Classe représentant un noeud contenant
    - 'etat', un état
    - 'parent', le prédécesseur du noeud, éventuellement None si aucun
    - 'action', l'action qui a conduit à ce noeud
    - 'g', le coût cumulé, 0 si aucun
    - 'critere', la fonction qui permet de calculer f à partir d'un noeud
    - 'f', le score utilisé pour piocher dans OPEN, g si aucun
    """
    def __init__(self, etat, g=None, critere=None, parent=None, action=None):
        self.etat = etat
        self.parent = parent
        self.action = action
        self.critere=critere
        if (g == None):
            self.g = 0
        else:
            self.g = g
        if (critere == None):
            self.critere = lambda noeud: noeud.g
        else:
            self.critere = critere

    def reconstruire_chemin(self):
        """
        Reconsruit le chemin depuis la racine de l'arbre d'exploration
        """
        noeud, p = self, []
        while noeud:
            p.append(noeud)
            noeud = noeud.parent
        return list(reversed(p))

    def creer_fils(self, action, probleme):
        """
        Crée un nouveau noeud à partir de l'actuel en appliquant une action donnée.
        L'action est supposée valable.
        """
        nouvel_etat = probleme.transition(self.etat, action)
        nouveau_g = self.g + probleme.cout(self.etat, action)
        return Noeud(nouvel_etat,\
                     parent=self,\
                     action=action,\
                     g=nouveau_g,
                     critere=self.critere)
 






    @property
    def f(self):
        return self.critere(self)

    def __str__(self):
        return str(self.etat)+" / "+str(self.f)

