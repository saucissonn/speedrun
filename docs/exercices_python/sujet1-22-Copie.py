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

def recherche(elt, tab):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def recherche(elt, tab):
    res = None
    for i in range(len(tab)):
        if tab[i] == elt:
            res = i
    return res
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert recherche(1, [8, 1, 10, 1, 7, 1, 8]) == 5
assert recherche(1, [2, 3, 4]) == None
assert recherche(1, [10, 12, 1, 56]) == 2
assert recherche(1, [1, 0, 42, 7]) == 0
assert recherche(1, [1, 50, 1]) == 2
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert recherche(1, [8, 1, 10, 1, 7, 1, 8]) == 5
assert recherche(1, [2, 3, 4]) == None
assert recherche(1, [10, 12, 1, 56]) == 2
assert recherche(1, [1, 0, 42, 7]) == 0
assert recherche(1, [1, 50, 1]) == 2
# --- PYODIDE:post --- #
##########################