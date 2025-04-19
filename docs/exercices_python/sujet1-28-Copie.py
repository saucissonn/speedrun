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

def a_doublon(lst):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def a_doublon(tab):
    for i in range(1, len(tab)):
        if tab[i-1] == tab[i]:
            return True
    return False
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert not a_doublon([])
assert not a_doublon([1])
assert a_doublon([1, 2, 4, 6, 6])
assert a_doublon([2, 5, 7, 7, 7, 9])
assert not a_doublon([0, 2, 3])
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert not a_doublon([])
assert not a_doublon([1])
assert a_doublon([1, 2, 4, 6, 6])
assert a_doublon([2, 5, 7, 7, 7, 9])
assert not a_doublon([0, 2, 3])
# --- PYODIDE:post --- #
##########################