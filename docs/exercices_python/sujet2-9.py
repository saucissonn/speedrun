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

def dichotomie(tab, x):
    """
    tab : tableau d'entiers trié dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = ... 
        if x == tab[m]:
            return ... 
        if x > tab[m]:
            debut = m + 1
        else:
            fin = ... 
    return ... 

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def dichotomie(tab, x):
    """
    tab : tableau d'entiers trié dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2 
        if x == tab[m]:
            return True 
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1 
    return False
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert multiplication(-2, 0) == 0
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28)
assert not dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert multiplication(-2, 0) == 0
assert dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28)
assert not dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27)
# --- PYODIDE:post --- #
##########################