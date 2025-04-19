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

def occurrences(elt, txt):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def occurrences(caractere, chaine):
    cpt = 0
    for c in chaine:
        if c == caractere :
            cpt = cpt + 1
    return cpt
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert occurrences('e', "sciences") == 2
assert occurrences('i',"mississippi") == 4
assert occurrences('a',"mississippi") == 0
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert occurrences('e', "sciences") == 2
assert occurrences('i',"mississippi") == 4
assert occurrences('a',"mississippi") == 0
# --- PYODIDE:post --- #
##########################