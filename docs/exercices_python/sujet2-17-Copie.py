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

def ajoute(indice, element, tab):
    '''Renvoie un nouveau tableau obtenu en insérant
    element à l'indice indice dans le tableau tab.'''
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)
    for i in range(indice):
        tab_ins[i] = ... 
    tab_ins[...] = ... 
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = ... 
    return tab_ins

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def ajoute(indice, element, tab):
    '''Renvoie un nouveau tableau obtenu en insÃ©rant
    element Ã  l'indice indice dans le tableau tab.'''
    nbre_elts = len(tab)
    tab_ins = [0] * (nbre_elts + 1)
    for i in range(indice):
        tab_ins[i] = tab[i] 
    tab_ins[indice] = element 
    for i in range(indice + 1, nbre_elts + 1):
        tab_ins[i] = tab[i-1] 
    return tab_ins
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert ajoute(1, 4, [7, 8, 9]) == [7, 4, 8, 9]
assert ajoute(3, 4, [7, 8, 9]) == [7, 8, 9, 4]
assert ajoute(0, 4, [7, 8, 9]) == [4, 7, 8, 9]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert ajoute(1, 4, [7, 8, 9]) == [7, 4, 8, 9]
assert ajoute(3, 4, [7, 8, 9]) == [7, 8, 9, 4]
assert ajoute(0, 4, [7, 8, 9]) == [4, 7, 8, 9]
# --- PYODIDE:post --- #
##########################