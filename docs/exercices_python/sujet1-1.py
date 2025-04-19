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

def voisins_entrants(adj, x):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def voisins_entrants(adj, x):
    t = []
    for i in range(len(adj)):
        if x in adj[i]:
            t.append(i)
    return t
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert voisins_entrants([[1, 2], [2], [0], [0]], 0) == [2, 3]
assert voisins_entrants([[1, 2], [2], [0], [0]], 1) == [0]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert voisins_entrants([[1, 2], [2], [0], [0]], 0) == [2, 3]
assert voisins_entrants([[1, 2], [2], [0], [0]], 1) == [0]
# --- PYODIDE:post --- #
##########################