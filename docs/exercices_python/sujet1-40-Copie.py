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

def recherche_indices_classement(v, lst):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def recherche_indices_classement(elt, tab):
    t_inf = []
    t_eq = []
    t_sup = []
    for i in range(len(tab)):
        if tab[i] == elt:
            t_eq.append(i)
        elif tab[i] < elt:
            t_inf.append(i)
        elif tab[i] > elt:
            t_sup.append(i)
    return (t_inf, t_eq, t_sup)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]) == ([0, 3, 7], [1, 6], [2, 4, 5])
assert recherche_indices_classement(3, [1, 4, 2, 4, 6, 0]) == ([0, 2, 5], [], [1, 3, 4])
assert recherche_indices_classement(3, [1, 1, 1, 1]) == ([0, 1, 2, 3], [], [])
assert recherche_indices_classement(3, []) == ([], [], [])
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]) == ([0, 3, 7], [1, 6], [2, 4, 5])
assert recherche_indices_classement(3, [1, 4, 2, 4, 6, 0]) == ([0, 2, 5], [], [1, 3, 4])
assert recherche_indices_classement(3, [1, 1, 1, 1]) == ([0, 1, 2, 3], [], [])
assert recherche_indices_classement(3, []) == ([], [], [])
# --- PYODIDE:post --- #
##########################