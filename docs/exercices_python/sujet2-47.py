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

def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = ... 
    tab[i] = ... 
    tab[j] = ... 

def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(...): 
        imin = ... 
        for i in range(..., N): 
            if tab[i] < ...: 
                imin = i
        echange(tab, ..., ...)

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i] 
    tab[i] = tab[j] 
    tab[j] = temp 

def tri_selection(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri par sélection.'''
    N = len(tab)
    for k in range(N-1): 
        imin = k 
        for i in range(k+1, N): 
            if tab[i] < tab[imin]: 
                imin = i
        echange(tab, k, imin)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
tab = [41, 55, 21, 18, 12, 6, 25]
tri_selection(tab)
assert tab == [6, 12, 18, 21, 25, 41, 55]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
tab = [41, 55, 21, 18, 12, 6, 25]
tri_selection(tab)
assert tab == [6, 12, 18, 21, 25, 41, 55]
# --- PYODIDE:post --- #
##########################