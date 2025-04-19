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

def crible(n):
    """Renvoie un tableau contenant tous les nombres premiers
    plus petits que n."""
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(n):
        if tab[i]:
            premiers.... 
            multiple = ... 
            while multiple < n:
                tab[multiple] = ... 
                multiple = ... 
    return premiers

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def crible(n):
    """Renvoie un tableau contenant tous les nombres premiers
    plus petits que n."""
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(n):
        if tab[i]:
            premiers.append(i) 
            multiple = 2*i 
            while multiple < n:
                tab[multiple] = False 
                multiple = multiple + i
    return premiers
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
assert crible(5) == [2, 3]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
assert crible(5) == [2, 3]
# --- PYODIDE:post --- #
##########################