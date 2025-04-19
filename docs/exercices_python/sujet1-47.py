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

a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
'H':['','']}

def taille(ABR, n):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def taille(arbre, lettre):
    if lettre == '':
        return 0
    return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert taille(a, 'F') == 9
assert taille(a, 'B') == 5
assert taille(a, 'I') == 2
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert taille(a, 'F') == 9
assert taille(a, 'B') == 5
assert taille(a, 'I') == 2
# --- PYODIDE:post --- #
##########################