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
    
def paire_6(tab):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
import random
def lancer(n):
    tlancer = []
    for i in range(n):
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
for i in range(5):
    assert 0 <= lancer1[i] <= 6
    assert len(lancer1) == 5
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
lancer1 = lancer(5)
for i in range(5):
    assert 0 <= lancer1[i] <= 6
    assert len(lancer1) == 5
lancer2 = lancer(1)
for i in range(1):
    assert 0 <= lancer2[i] <= 6
    assert len(lancer2) == 1
lancer3 = lancer(6)
while not lancer3.count(6) > 1:
    lancer3 = lancer(6)
assert paire_6(lancer3)
    
# --- PYODIDE:post --- #
##########################