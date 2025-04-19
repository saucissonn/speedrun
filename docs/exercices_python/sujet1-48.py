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

def recherche(lst, v):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def recherche(tab, n):
    ind = None
    for i in range(len(tab)):
        if tab[i] == n:
            ind = i
    return ind
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert recherche([5, 3],1) == None
assert recherche([2,4],2) == 0
assert recherche([2,3,5,2,4],2) == 3
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert recherche([5, 3],1) == None
assert recherche([2,4],2) == 0
assert recherche([2,3,5,2,4],2) == 3
# --- PYODIDE:post --- #
##########################