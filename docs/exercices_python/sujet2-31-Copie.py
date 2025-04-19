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

def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj 
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    if x ...: 
        acc.append(x)
        for y in ...: 
            parcours(adj, ...) 

def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, ...) 
    return acc

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj 
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    if x not in acc: 
        acc.append(x)
        for y in adj[x]: 
            parcours(adj, y, acc) 

def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, x, acc) 
    return acc
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert accessibles([[1, 2], [0, 3], [0], [1], [5], [4]], 0) == [0, 1, 3, 2]
assert accessibles([[1, 2], [0, 3], [0], [1], [5], [4]], 4) == [4, 5]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert accessibles([[1, 2], [0, 3], [0], [1], [5], [4]], 0) == [0, 1, 3, 2]
assert accessibles([[1, 2], [0, 3], [0], [1], [5], [4]], 4) == [4, 5]
# --- PYODIDE:post --- #
##########################