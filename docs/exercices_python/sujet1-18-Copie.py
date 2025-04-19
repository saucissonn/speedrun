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

def moyenne(lst):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def moyenne(tab):
    s = 0
    for v in tab:
        s = s + v
    return s / len(tab)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert moyenne([1]) == 1.0
assert moyenne([1, 2, 3, 4, 5, 6, 7]) == 4.0
assert moyenne([1, 2]) == 1.5
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert moyenne([1]) == 1.0
assert moyenne([1, 2, 3, 4, 5, 6, 7]) == 4.0
assert moyenne([1, 2]) == 1.5
# --- PYODIDE:post --- #
##########################