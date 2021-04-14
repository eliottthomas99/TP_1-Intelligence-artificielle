import time
from noeud import Noeud
from exploration import Exploration
from labyrinthe.probleme import Probleme
from labyrinthe.etat import Etat

plateau = [[3,0,0],[0,1,1],[0,0,2]]

but = [[0,0,0],[0,1,1],[0,2,3]]


etat_cible = Etat(but)

etat_initial = Etat(plateau)
# OU
#etat_initial = Probleme.melanger(etat_cible)

probleme = Probleme(etat_initial=etat_initial, etat_final=etat_cible)

#print("new heuristique")
#print(probleme.nombre_piece_mal_placees(etat_initial))

# Dijkstra
#fonction_score = lambda noeud: noeud.g
fonction_score = lambda noeud: noeud.g

#Greedy
greedy = lambda noeud: probleme.heuristique_manhattan(noeud.etat)


#A*
astar = lambda noeud: noeud.g + probleme.heuristique_manhattan(noeud.etat)


#Greedy nb pièces mal placées
greedyNbPieces = lambda noeud: probleme.nombre_piece_mal_placees(noeud.etat)



###############################################
# Exploration (générique)
###############################################

#exploration = Exploration(probleme=probleme, critere=fonction_score)
exploration = Exploration(probleme=probleme, critere=fonction_score)


temps_debut = time.process_time()
chemin = exploration.explorer()
temps_fin = time.process_time()

###############################################
# Résultat
###############################################
print("=====================================================")
etapes = -1
print("État initial :\t" + str(probleme.etat_initial))
if len(chemin) > 0:
    last = None
    for node in chemin:
        print(node.action)
        node.etat.afficher()
        time.sleep(0.2)
        last = node
        etapes += 1
        print(last)
    print("État final :\t\t" + str(last.etat))
    print("Coût total :\t\t" + str(last.g))
else:
    print("But non atteignable")

print("Nb de noeuds explorés :" + str(exploration.n_explores))
print("Nombre d'étapes: " + str(etapes))
print("Durée de l'exploration: " + str(temps_fin - temps_debut) + " second(s)") 
