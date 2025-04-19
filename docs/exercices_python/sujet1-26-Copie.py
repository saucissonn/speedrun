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

def ajoute_dictionnaires(d1, d2):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def ajoute_dictionnaires(d1, d2):
    d = {}
    for k in d1:
        if k in d2 :
            d[k] = d1[k] + d2[k]
        else :
            d[k] = d1[k]
    for k in d2:
        if k not in d:
            d[k] = d2[k]
    return d
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}) == {1: 5, 2: 16, 3: 11}
assert ajoute_dictionnaires({}, {2: 9, 3: 11}) == {2: 9, 3: 11}
assert ajoute_dictionnaires({1: 5, 2: 7}, {}) == {1: 5, 2: 7}
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}) == {1: 5, 2: 16, 3: 11}
assert ajoute_dictionnaires({}, {2: 9, 3: 11}) == {2: 9, 3: 11}
assert ajoute_dictionnaires({1: 5, 2: 7}, {}) == {1: 5, 2: 7}
# --- PYODIDE:post --- #
##########################