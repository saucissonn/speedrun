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

def delta(liste):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def delta(liste):
    t = [liste[0]]
    for i in range(1, len(liste)):
        t.append(liste[i] - liste[i-1])
    return t
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert delta([1000, 800, 802, 1000, 1003]) == [1000, -200, 2, 198, 3]
assert delta([42]) == [42]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert delta([1000, 800, 802, 1000, 1003]) == [1000, -200, 2, 198, 3]
assert delta([42]) == [42]
# --- PYODIDE:post --- #
##########################