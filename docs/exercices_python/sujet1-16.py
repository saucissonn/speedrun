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
def moyenne(notes):
    s = 0
    coef = 0
    for c in notes:
        s = s + c[0]*c[1]
        coef = coef + c[1]
    return s / coef
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert moyenne([(15.0,2),(9.0,1),(12.0,3)]) == 12.5
assert ligne_suivante([1, 3, 3, 1]) == [1, 4, 6, 4, 1]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert moyenne([(15.0,2),(9.0,1),(12.0,3)]) == 12.5
assert ligne_suivante([1, 3, 3, 1]) == [1, 4, 6, 4, 1]
# --- PYODIDE:post --- #
##########################