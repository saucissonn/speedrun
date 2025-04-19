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

valeurs = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return ... 
    v = valeurs[rang]
    if v <= ...: 
        return ... + rendu_glouton(a_rendre - v, rang) 
    else:
        return rendu_glouton(a_rendre, ...)

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
valeurs = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return [] 
    v = valeurs[rang]
    if v <= a_rendre: 
        return [v] + rendu_glouton(a_rendre - v, rang) 
    else:
        return rendu_glouton(a_rendre, rang+1)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert rendu_glouton(67, 0) == [50, 10, 5, 2]
assert rendu_glouton(291, 0) == [100, 100, 50, 20, 20, 1]
assert rendu_glouton(291,1) == [50, 50, 50, 50, 50, 20, 20, 1]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert rendu_glouton(67, 0) == [50, 10, 5, 2]
assert rendu_glouton(291, 0) == [100, 100, 50, 20, 20, 1]
assert rendu_glouton(291,1) == [50, 50, 50, 50, 50, 20, 20, 1]
# --- PYODIDE:post --- #
##########################