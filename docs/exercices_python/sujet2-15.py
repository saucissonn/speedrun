# --- PYODIDE:ignore --- #
##########################
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

def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab, 
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // ... 
    if ... < x: 
        return chercher(tab, x, ... , ...) 
    elif tab[m] > x:
        return chercher(tab, x, ... , ...) 
    else:
        return ... 

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab, 
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // 2 
    if tab[m] < x: 
        return chercher(tab, x, m+1 , j) 
    elif tab[m] > x:
        return chercher(tab, x, i , m-1)  
    else:
        return m
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
chercher([1, 5, 6, 6, 9, 12], 7, 0, 5)
assert chercher([1, 5, 6, 6, 9, 12], 9, 0, 5) == 4
assert chercher([1, 5, 6, 6, 9, 12], 6, 0, 5) == 2
chercher([1], 0, 0, 0)
assert chercher([1], 1, 0, 0) == 0
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
chercher([1, 5, 6, 6, 9, 12], 7, 0, 5)
assert chercher([1, 5, 6, 6, 9, 12], 9, 0, 5) == 4
assert chercher([1, 5, 6, 6, 9, 12], 6, 0, 5) == 2
chercher([1], 0, 0, 0)
assert chercher([1], 1, 0, 0) == 0
# --- PYODIDE:post --- #
##########################