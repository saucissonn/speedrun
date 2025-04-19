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

def nb_repetitions(v, lst):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def nb_repetitions(elt, tab):
    cpt = 0
    for e in tab:
        if e == elt:
            cpt = cpt + 1
    return cpt
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]) == 3
assert nb_repetitions('A', ['B', 'A', 'B', 'A', 'R']) == 2
assert nb_repetitions(12, [1, '!', 7, 21, 36, 44]) == 0
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]) == 3
assert nb_repetitions('A', ['B', 'A', 'B', 'A', 'R']) == 2
assert nb_repetitions(12, [1, '!', 7, 21, 36, 44]) == 0
# --- PYODIDE:post --- #
##########################