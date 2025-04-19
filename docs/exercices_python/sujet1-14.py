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

def lancer(n):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
import random
def lancer(n):
    tlancer = []
    for i in range(6):
        tlancer.append(random.randint(1,6))
    return tlancer

def paire_6(tab):
    cpt = 0
    for v in tab:
        if v == 6:
            cpt = cpt + 1
    return cpt >= 2
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
lancer1 = lancer(5)
assert lancer1 == [5, 6, 6, 2, 2]
assert paire_6(lancer1)
lancer2 = lancer(5)
assert lancer2 == [6, 5, 1, 6, 6]
assert paire_6(lancer2)
lancer3 = lancer(3)
assert lancer3 == [2, 2, 6]
assert not paire_6(lancer3)
lancer4 = lancer(0)
assert lancer4 == []
assert not paire_6(lancer4)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
lancer1 = lancer(5)
assert lancer1 == [5, 6, 6, 2, 2]
assert paire_6(lancer1)
lancer2 = lancer(5)
assert lancer2 == [6, 5, 1, 6, 6]
assert paire_6(lancer2)
lancer3 = lancer(3)
assert lancer3 == [2, 2, 6]
assert not paire_6(lancer3)
lancer4 = lancer(0)
assert lancer4 == []
assert not paire_6(lancer4)
# --- PYODIDE:post --- #
##########################