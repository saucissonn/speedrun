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

def liste_puissances(n, p):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def liste_puissances(a,n):
    t = [a]
    for i in range(1, n):
        t.append(a*t[i-1])
    return t

def liste_puissances_borne(a, borne):
    if a >= borne:
        return []
    t = [a]
    i = 1
    while a*t[i-1] < borne:
        t.append(a*t[i-1])
        i = i + 1
    return t
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert liste_puissances(3, 5) == [3, 9, 27, 81, 243]
assert liste_puissances(-2, 4) == [-2, 4, -8, 16]
assert liste_puissances_borne(2, 16) == [2, 4, 8]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert liste_puissances(3, 5) == [3, 9, 27, 81, 243]
assert liste_puissances(-2, 4) == [-2, 4, -8, 16]
assert liste_puissances_borne(2, 16) == [2, 4, 8]
# --- PYODIDE:post --- #
##########################