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

def gb_vers_entier(lst):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def gb_vers_entier(tab):
    s = 0
    n = len(tab)
    for i in range(n):
        v = tab[n - 1 - i]
        if v :
            s = s + 2**i
    return s
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert gb_vers_entier([]) == 0
assert gb_vers_entier([True]) == 1
assert gb_vers_entier([True, False, True, False, False, True, True]) == 83
assert gb_vers_entier([True, False, False, False, False, False, True, False]) == 130
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert gb_vers_entier([]) == 0
assert gb_vers_entier([True]) == 1
assert gb_vers_entier([True, False, True, False, False, True, True]) == 83
assert gb_vers_entier([True, False, False, False, False, False, True, False]) == 130
# --- PYODIDE:post --- #
##########################