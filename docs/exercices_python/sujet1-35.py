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

def max_dico(dico):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def max_dico(dico):
    lmax = 0
    nom = ""
    for k,v in dico.items():
        if v > lmax:
            lmax = v
            nom = k
    return (nom, lmax)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert max_dico({ 'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50 }) == ('Ada', 201)
assert max_dico({ 'Alan': 222, 'Ada': 201, 'Eve': 222, 'Tim': 50 }) == ('Alan', 222)
assert not self.est_vide()
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert max_dico({ 'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50 }) == ('Ada', 201)
assert max_dico({ 'Alan': 222, 'Ada': 201, 'Eve': 222, 'Tim': 50 }) == ('Alan', 222)
assert not self.est_vide()
# --- PYODIDE:post --- #
##########################