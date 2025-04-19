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

def tri_bulles(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles.'''
    n = len(tab)
    for i in range(...): 
        for j in range(...): 
            if ... > ...: 
                echange(tab, j, ...)

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

def tri_bulles(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles.'''
    n = len(tab)
    for i in range(n-1): 
        for j in range(n-i-1): 
            if tab[j] > tab[j+1]: 
                echange(tab, j, j+1)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
tab = []
tri_bulles(tab)
assert tab == []
tab2 = [9, 3, 7, 2, 3, 1, 6]
tri_bulles(tab2)
assert tab2 == [1, 2, 3, 3, 6, 7, 9]
tab3 = [9, 7, 4, 3]
tri_bulles(tab3)
assert tab3 == [3, 4, 7, 9]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
tab = []
tri_bulles(tab)
assert tab == []
tab2 = [9, 3, 7, 2, 3, 1, 6]
tri_bulles(tab2)
assert tab2 == [1, 2, 3, 3, 6, 7, 9]
tab3 = [9, 7, 4, 3]
tri_bulles(tab3)
assert tab3 == [3, 4, 7, 9]
# --- PYODIDE:post --- #
##########################