import collections
import sys
from noeud import *

class Exploration:
    """
    Algorithme d'exploration
    - probleme : Problème formalisé à résoudre
    - critere : fonction qui associe un noeud à un score, le plus faible étant le meilleur
    - open : collection de noeuds connus mais pas encore explorés
    - close : collection de noeuds déjà explorés
    - n_explores : nombre de noeuds explorés (utile pour les statistiques à la fin)
    """

    def __init__(self, probleme, critere):
        self.probleme = probleme
        self.critere = critere
        self.open = dict()
        self.close = dict()
        self.n_explores = 0

    def piocher(self):
        """
        Renvoie un nouveau noeud à explorer
        """

        min = 10**8

        for nodeKey in self.open.keys():
            #if(self.open[nodeKey].g < min):
            #print(self.open[nodeKey].etat)
            if(self.critere(self.open[nodeKey]) < min):    
                #min = self.open[nodeKey].g
                min = self.critere(self.open[nodeKey])
                minindice = nodeKey

        minode = self.open[minindice]
        del self.open[minindice]


        #print("minode", minode)
        return minode


    def mettre_a_jour_arbre(self, nouveaux_noeuds):
        """
        Met à jour l'arbre d'exploration avec un nouveau noeud
        """
        # À implémenter
        for nouveau in nouveaux_noeuds:
            if nouveau.etat in self.close.keys():
                #if(    nouveau.g <= self.close[nouveau.etat].g  ):
                if(    self.critere(nouveau) < self.critere(self.close[nouveau.etat])  ):
                    """
                    print("close")
                    self.printclose()
                    print("nouveau")
                    print(nouveau)
                    
                    print("before")
                    print(self.close[nouveau.etat])
                    """

                    del self.close[ self.close[nouveau.etat].etat ]
                    self.open[nouveau.etat] = nouveau
                    #print("plusopen")
                #else:
                    #print("raté1")


            else:
                if(nouveau.etat in self.open.keys()):



                    #if(    nouveau.g <= self.open[nouveau.etat].g   ): #where is the ancient node ?
                    if(    self.critere(nouveau) <  self.critere(self.open[nouveau.etat])   ): #where is the ancient node ?



                        self.open[nouveau.etat] = nouveau
                        #print("plusopen2")
                    #else: 
                        #print("raté2")

                else:
                    self.open[nouveau.etat] = nouveau
                    #print("plusopen3")







    def explorer(self):


        etatInit = self.probleme.etat_initial


        self.open[etatInit]=Noeud(etatInit, critere=self.critere)


        #print("open" , self.open)

        while(self.open != {}): #tant que open n'est pas vide
            """
            print("openDeb")
            self.printopen()
           """
            noeud_courant = self.piocher()

            #print("openaprespioch", self.open)
            #print(noeud_courant)
            #print(self.probleme.etat_final)

            self.close[noeud_courant.etat]=noeud_courant

            if(      self.probleme.but(noeud_courant.etat)   ):
                print("solution ?")
                return self.makeSolution()

            else:

                nouveaux_noeuds = []
                for actionPos in self.probleme.actions_possibles(noeud_courant.etat):
                    nodeToadd = noeud_courant.creer_fils(actionPos, self.probleme)
                    #print("toadd", nodeToadd)
                    nouveaux_noeuds.append( nodeToadd  )
                #print("nouveaux : ",nouveaux_noeuds)



                #print("avant MAJ", self.open)
                self.mettre_a_jour_arbre(nouveaux_noeuds)
                #print("apres MAJ", self.open)
            """
            print("openFin")
            self.printopen()
            """

        """
        Explore un espace d'état et retourne le chemin trouvé,
        éventuellement None si aucun chemin n'est trouvé
        """
        # À implémenter
        return None


    def makeSolution(self):
        node = self.close[self.probleme.etat_final]

        res = []

        while(node !=  None ):
            res.append(node)
            node = node.parent
        return res[::-1]

    def printopen(self):
        for key in self.open.keys():
            print(self.open[key])
    def printclose(self):
        print("----------------------")
        for key in self.close.keys():
            print("key")
            print(key)
            print("value")
            print(self.close[key])
        print("----------------------")

