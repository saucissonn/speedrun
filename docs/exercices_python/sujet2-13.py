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

def insere(tab, a):
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    tab_a = [ a ] + tab # nouveau tableau contenant a 
                        # suivi des éléments de tab
    i = 0
    while i < ... and a > ...: 
        tab_a[i] = ... 
        tab_a[i+1] = a
        i = ... 
    return tab_a

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def insere(tab, a):
    """
    Insère l'élément a (int) dans le tableau tab (list)
    trié par ordre croissant à sa place et renvoie le
    nouveau tableau.
    """
    tab_a = [ a ] + tab # nouveau tableau contenant a 
                        # suivi des éléments de tab
    i = 0
    while i < len(tab) and a > tab[i]: 
        tab_a[i] = tab_a[i+1]  
        tab_a[i+1] = a
        i = i + 1 
    return tab_a
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert insere([1, 2, 4, 5], 3) == [1, 2, 3, 4, 5]
assert insere([1, 2, 7, 12, 14, 25], 30) == [1, 2, 7, 12, 14, 25, 30]
assert insere([2, 3, 4], 1) == [1, 2, 3, 4]
assert insere([], 1) == [1]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert insere([1, 2, 4, 5], 3) == [1, 2, 3, 4, 5]
assert insere([1, 2, 7, 12, 14, 25], 30) == [1, 2, 7, 12, 14, 25, 30]
assert insere([2, 3, 4], 1) == [1, 2, 3, 4]
assert insere([], 1) == [1]
# --- PYODIDE:post --- #
##########################