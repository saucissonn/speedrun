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

def verifie(lst):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def verifie(tab):
    n = len(tab)
    if n < 2 :
        return True
    for i in range(1,n) :
        if tab[i] < tab[i-1] :
            return False
    return True
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert verifie([0, 5, 8, 8, 9])
assert not verifie([8, 12, 4])
assert verifie([-1, 4])
assert verifie([])
assert verifie([5])
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert verifie([0, 5, 8, 8, 9])
assert not verifie([8, 12, 4])
assert verifie([-1, 4])
assert verifie([])
assert verifie([5])
# --- PYODIDE:post --- #
##########################