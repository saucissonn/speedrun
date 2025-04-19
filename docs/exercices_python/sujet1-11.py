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

def parcours_largeur(ABR):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def parcours_largeur(arb):
    file = [arb]
    t = []
    while len(file) != 0:
        x = file.pop(0)
        t.append(x[1])
        if x[0] != None:
            file.append(x[0])
        if x[2] != None:
            file.append(x[2])
    return t
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert parcours_largeur(arbre) == [4, 2, 6, 1, 3, 5, 7]
assert somme_max([1, 2, 3, 4, 5]) == 15
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert parcours_largeur(arbre) == [4, 2, 6, 1, 3, 5, 7]
assert somme_max([1, 2, 3, 4, 5]) == 15
# --- PYODIDE:post --- #
##########################