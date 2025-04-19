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

def enumere(lst):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def enumere(tab):
    d = {}
    for i in range(len(tab)):
        if tab[i] not in d:
            d[tab[i]] = [i]
        else :
            d[tab[i]].append(i)
    return d
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert enumere([]) == {}
assert enumere([1, 2, 3]) == {1: [0], 2: [1], 3: [2]}
assert enumere([1, 1, 2, 3, 2, 1]) == {1: [0, 1, 5], 2: [2, 4], 3: [3]}
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert enumere([]) == {}
assert enumere([1, 2, 3]) == {1: [0], 2: [1], 3: [2]}
assert enumere([1, 1, 2, 3, 2, 1]) == {1: [0, 1, 5], 2: [2, 4], 3: [3]}
# --- PYODIDE:post --- #
##########################