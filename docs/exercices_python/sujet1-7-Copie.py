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

def nbr_occurrences(txt):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def nbr_occurrences(chaine):
    d = {}
    for c in chaine:
        if c in d:
            d[c] = d[c] + 1
        else :
            d[c] = 1
    return d
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert nbr_occurrences("Hello world !") == {'H': 1,'e': 1,'l': 3,'o': 2,' ': 2,'w': 1,'r': 1,'d': 1,'!': 1}
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert nbr_occurrences("Hello world !") == {'H': 1,'e': 1,'l': 3,'o': 2,' ': 2,'w': 1,'r': 1,'d': 1,'!': 1}
# --- PYODIDE:post --- #
##########################