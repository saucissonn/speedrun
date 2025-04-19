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

def ou_exclusif(l1, l2):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def ou_exclusif(t1, t2):
    t = []
    for i in range(len(t1)):
        if t1[i] == t2[i]:
            t.append(0)
        else:
            t.append(1)
    return t
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert ou_exclusif([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0]) == [1, 1, 0, 1, 1, 0, 0, 1]
assert ou_exclusif([1, 1, 0, 1], [0, 0, 1, 1]) == [1, 1, 1, 0]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert ou_exclusif([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0]) == [1, 1, 0, 1, 1, 0, 0, 1]
assert ou_exclusif([1, 1, 0, 1], [0, 0, 1, 1]) == [1, 1, 1, 0]
# --- PYODIDE:post --- #
##########################