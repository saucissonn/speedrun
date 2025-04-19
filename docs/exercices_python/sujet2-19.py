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

def separe(tab):
    '''Separe les 0 et les 1 dans le tableau tab'''
    gauche = 0
    droite = ... 
    while gauche < droite:
        if tab[gauche] == 0 :
            gauche = ... 
        else :
            tab[gauche] = ... 
            tab[droite] = ... 
            droite = ... 
    return tab

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def separe(tab):
    '''Separe les 0 et les 1 dans le tableau tab'''
    gauche = 0
    droite = len(tab) - 1 
    while gauche < droite:
        if tab[gauche] == 0 :
            gauche = gauche + 1 
        else :
            tab[gauche] = tab[droite] 
            tab[droite] = 1 
            droite = droite - 1 
    return tab
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert recherche_min([-1, -2, -3, -3]) == 2
assert separe([1, 0, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 1, 1, 1, 1]
assert separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]) == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert recherche_min([-1, -2, -3, -3]) == 2
assert separe([1, 0, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 1, 1, 1, 1]
assert separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]) == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# --- PYODIDE:post --- #
##########################