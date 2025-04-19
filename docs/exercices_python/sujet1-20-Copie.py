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

def min_et_max(lst):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def min_et_max(tab):
    vmin = tab[0]
    vmax = tab[0]
    for v in tab:
        if v > vmax:
            vmax = v
        if v < vmin:
            vmin = v
    return {"min":vmin, "max":vmax}
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {'min': -2, 'max': 9}
assert min_et_max([0, 1, 2, 3]) == {'min': 0, 'max': 3}
assert min_et_max([3]) == {'min': 3, 'max': 3}
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]) == {'min': -2, 'max': 9}
assert min_et_max([0, 1, 2, 3]) == {'min': 0, 'max': 3}
assert min_et_max([3]) == {'min': 3, 'max': 3}
# --- PYODIDE:post --- #
##########################