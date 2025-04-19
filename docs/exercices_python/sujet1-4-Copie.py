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

def ecriture_binaire_entier_positif(n):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def ecriture_binaire_entier_positif(n):
    vbin = str(n%2)
    n = n // 2
    while n > 0:
        vbin = str(n%2) + vbin
        n = n //2
    return vbin
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert ecriture_binaire_entier_positif(0) == '0'
assert ecriture_binaire_entier_positif(2) == '10'
assert ecriture_binaire_entier_positif(105) == '1101001'
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert ecriture_binaire_entier_positif(0) == '0'
assert ecriture_binaire_entier_positif(2) == '10'
assert ecriture_binaire_entier_positif(105) == '1101001'
# --- PYODIDE:post --- #
##########################