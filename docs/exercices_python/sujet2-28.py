# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:env --- #
class Stack:
    """ (Interface à décrire dans l'énoncé) """
    def __init__(self): self.__stk=[]
    def push(self, v): self.__stk.append(v)
    def pop(self): return self.__stk.pop()
    def is_empty(self): return not self.__stk
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:code --- #

def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(...): 
        if s[i] == chiffre:
            compte = ... 
        else:
            resultat += ... + ... 
            chiffre = ... 
            ...
    lecture_... = ... + ... 
    resultat += lecture_chiffre
    return resultat

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def voisinage(n, ligne, colonne):
    """ Renvoie la liste des coordonnées des voisins de la case
    (ligne, colonne) en gérant les cases sur les bords. """
    voisins = []
    for l in range(max(0,ligne-1), min(n, ligne+2)):
        for c in range(max(0, colonne-1), min(n, colonne+2)):
            if (l, c) != (ligne, colonne):
                voisins.append((l,c))
    return voisins

def incremente_voisins(grille, ligne, colonne):
    """ Incrémente de 1 toutes les cases voisines d'une bombe."""
    voisins = voisinage(len(grille), ligne, colonne) 
    for l, c in voisins:
        if grille[l][c] != -1: # si ce n'est pas une bombe 
            grille[l][c] += 1  # on ajoute 1 à sa valeur 

def genere_grille(bombes):
    """ Renvoie une grille de démineur de taille nxn où n est
    le nombre de bombes, en plaçant les bombes à l'aide de
    la liste bombes de coordonnées (tuples) passée en
    paramètre. """
    n = len(bombes)
    # Initialisation d'une grille nxn remplie de 0
    grille = [[0 for colonne in range(n)] for ligne in range(n)]
    # Place les bombes et calcule les valeurs des autres cases
    for ligne, colonne in bombes:
        grille[ligne][colonne] = -1 # place la bombe 
        incremente_voisins(grille, ligne, colonne)  # incrémente ses voisins 
    return grille
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert genere_grille([(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)]) == [[1, 1, 1, 0, 0],
                                                                [1, -1, 1, 1, 1],
                                                                [2, 2, 3, 2, -1],
                                                                [1, -1, 2, -1, 3],
                                                                [1, 1, 2, 2, -1]]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert genere_grille([(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)]) == [[1, 1, 1, 0, 0],
                                                                [1, -1, 1, 1, 1],
                                                                [2, 2, 3, 2, -1],
                                                                [1, -1, 2, -1, 3],
                                                                [1, 1, 2, 2, -1]]
# --- PYODIDE:post --- #
##########################