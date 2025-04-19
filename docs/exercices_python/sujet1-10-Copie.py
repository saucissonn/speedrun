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

def recherche(lst):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def recherche(tab, n):
    i = 0
    j = len(tab)-1
    while j >= i :
        mil = (i+j)//2
        if tab[mil] == n:
            return mil
        elif tab[mil] > n:
            j = mil - 1
        else :
            i = mil + 1
    return None



# la version récursive est aussi possible :

def recherche_rec(tab, n):
    def search(tab, n, i, j):
        if j < i :
            return None
        mil = (i + j) // 2
        if tab[mil] == n :
            return mil
        elif tab[mil] > n :
            return search(tab, n, i, mil-1)
        else :
            return search(tab, n, mil+1, j)
    return search(tab,n, 0, len(tab)-1)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert recherche([2, 3, 4, 5, 6], 5) == 3
assert recherche([2, 3, 4, 6, 7], 5) == None
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert recherche([2, 3, 4, 5, 6], 5) == 3
assert recherche([2, 3, 4, 6, 7], 5) == None
# --- PYODIDE:post --- #
##########################