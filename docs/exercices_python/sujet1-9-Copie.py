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

def multiplication(a, b):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def multiplication(n1, n2):
    if n1 < 0 and n2 > 0 :
        return -multiplication(-n1, n2)
    if n1 > 0 and n2 < 0 :
        return -multiplication(n1, -n2)
    if n1 < 0 and n2 < 0 :
        return multiplication(-n1, -n2)
    s = 0
    for i in range(n1):
        s = s + n2
    return s
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert multiplication(3, 5) == 15
assert multiplication(-4, -8) == 32
assert multiplication(-2, 6) == -12
assert multiplication(-2, 0) == 0
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert multiplication(3, 5) == 15
assert multiplication(-4, -8) == 32
assert multiplication(-2, 6) == -12
assert multiplication(-2, 0) == 0
# --- PYODIDE:post --- #
##########################