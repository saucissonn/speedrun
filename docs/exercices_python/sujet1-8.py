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

def maximum_tableau(lst):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def maximum_tableau(tab):
    vmax = tab[0]
    for v in tab:
        if v > vmax:
            vmax = v
    return vmax
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert maximum_tableau([98, 12, 104, 23, 131, 9]) == 131
assert maximum_tableau([-27, 24, -3, 15]) == 24
        assert not self.est_vide()
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert maximum_tableau([98, 12, 104, 23, 131, 9]) == 131
assert maximum_tableau([-27, 24, -3, 15]) == 24
        assert not self.est_vide()
# --- PYODIDE:post --- #
##########################