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

def colore_comp1(M, i, j, val):
    if M[i][j] != 1:
        return

    M[i][j] = val

    if i-1 >= 0: # propage en haut
        colore_comp1(M, i-1, j, val)
    if ... < len(M): # propage en bas 
        colore_comp1(M, ..., j, val) 
    if ...: # propage à gauche 
        colore_comp1(M, ..., ..., val) 
    if ...: # propage à droite 
        ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def colore_comp1(M, i, j, val):
    if M[i][j] != 1:
        return

    M[i][j] = val

    if i-1 >= 0: # propage à gauche
        colore_comp1(M, i-1, j, val)
    if i+1 < len(M): # propage à droite 
        colore_comp1(M, i+1, j, val) 
    if j-1 >= 0 : # propage en haut 
        colore_comp1(M, i, j-1, val) 
    if j+1 < len(M[0]): # propage en bas 
        colore_comp1(M, i, j+1, val)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
colore_comp1(M, 2, 1, 3)
assert M == [[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
colore_comp1(M, 2, 1, 3)
assert M == [[0, 0, 1, 0], [0, 3, 0, 1], [3, 3, 3, 0], [0, 3, 3, 0]]
# --- PYODIDE:post --- #
##########################