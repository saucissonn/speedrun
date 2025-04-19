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

def moyenne(lst):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def moyenne (tab):
    s_coef = 0
    s_note = 0
    for t in tab:
        s_coef = s_coef + t[1]
        s_note = s_note + t[0]*t[1]
    if s_coef == 0:
        return None
    else :
        return s_note / s_coef
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]) == 9.142857142857142
assert moyenne([(3, 0), (5, 0)]) == None
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]) == 9.142857142857142
assert moyenne([(3, 0), (5, 0)]) == None
# --- PYODIDE:post --- #
##########################