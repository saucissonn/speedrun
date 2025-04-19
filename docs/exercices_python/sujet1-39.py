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
    N = len(tab)
    assert N != 0, "le tableau ne doit pas être vide"
    s = 0
    for v in tab:
        s = s + v
    return s / N
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert moyenne([5,3,8]) == 5.333333333333333
assert moyenne([1,2,3,4,5,6,7,8,9,10]) == 5.5
assert moyenne([]) == None # Comportement différent suivant le traitement proposé.
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert moyenne([5,3,8]) == 5.333333333333333
assert moyenne([1,2,3,4,5,6,7,8,9,10]) == 5.5
assert moyenne([]) == None # Comportement différent suivant le traitement proposé.
# --- PYODIDE:post --- #
##########################