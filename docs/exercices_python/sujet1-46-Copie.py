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

def compte_occurrences(v, lst):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def compte_occurrences(x, tab):
    cpt = 0
    for v in tab:
        if v == x:
            cpt = cpt + 1
    return cpt
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert compte_occurrences(5, []) == 0
assert compte_occurrences(5, [-2, 3, 1, 5, 3, 7, 4]) == 1
assert compte_occurrences('a', ['a','b','c','a','d','e','a']) == 3
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert compte_occurrences(5, []) == 0
assert compte_occurrences(5, [-2, 3, 1, 5, 3, 7, 4]) == 1
assert compte_occurrences('a', ['a','b','c','a','d','e','a']) == 3
# --- PYODIDE:post --- #
##########################