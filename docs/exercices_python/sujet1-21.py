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

def indices_maxi(lst):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def indices_maxi(tab):
    nmax = tab[0]
    tindice = [0]
    for i in range(1, len(tab)) :
        if tab[i] > nmax :
            nmax = tab[i]
            tindice = [i]
        elif tab[i] == nmax :
            tindice.append(i)
    return (nmax, tindice)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, [3, 8])
assert indices_maxi([7]) == (7, [0])
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, [3, 8])
assert indices_maxi([7]) == (7, [0])
# --- PYODIDE:post --- #
##########################