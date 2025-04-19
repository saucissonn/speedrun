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

def recherche_min(lst):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def recherche_min(tab):
    vmin = tab[0]
    imin = 0
    for i in range(1, len(tab)):
        if tab[i] < vmin:
            vmin = tab[i]
            imin = i
    return imin
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert recherche_min([5]) == 0
assert recherche_min([2, 4, 1]) == 2
assert recherche_min([5, 3, 2, 2, 4]) == 2
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert recherche_min([5]) == 0
assert recherche_min([2, 4, 1]) == 2
assert recherche_min([5, 3, 2, 2, 4]) == 2
# --- PYODIDE:post --- #
##########################