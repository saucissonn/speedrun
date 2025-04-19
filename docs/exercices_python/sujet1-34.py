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

def tri_selection(lst):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def tri_selection(tab):
    N = len(tab)
    for i in range(N-1):
        imin = i
        for j in range (i+1,N):
            if tab[j] < tab[imin]:
                imin = j
        if imin != i:
            tab[i], tab[imin] = tab[imin], tab[i]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
tab = [1, 52, 6, -9, 12]
tri_selection(tab)
assert tab == [-9, 1, 6, 12, 52]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
tab = [1, 52, 6, -9, 12]
tri_selection(tab)
assert tab == [-9, 1, 6, 12, 52]
# --- PYODIDE:post --- #
##########################