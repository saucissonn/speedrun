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

def max_et_indice(lst):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def max_et_indice(tab):
    imax = 0
    vmax = tab[0]
    for i in range(len(tab)):
        if tab[i] > vmax:
            vmax = tab[i]
            imax = i
    return (vmax, imax)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)
assert max_et_indice([-2]) == (-2, 0)
assert max_et_indice([-1, -1, 3, 3, 3]) == (3, 2)
assert max_et_indice([1, 1, 1, 1]) == (1, 0)
    assert ... 
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)
assert max_et_indice([-2]) == (-2, 0)
assert max_et_indice([-1, -1, 3, 3, 3]) == (3, 2)
assert max_et_indice([1, 1, 1, 1]) == (1, 0)
    assert ... 
# --- PYODIDE:post --- #
##########################