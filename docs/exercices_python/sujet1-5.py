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
def renverse(txt):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def renverse(mot):
    s = ""
    for c in mot:
        s = c + s
    return s
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert renverse("") == ""
assert renverse("abc") == "cba"
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert renverse("") == ""
assert renverse("abc") == "cba"
# --- PYODIDE:post --- #
##########################