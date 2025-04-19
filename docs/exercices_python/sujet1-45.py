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

def correspond(txt1, txt2):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def correspond(mot, mot_a_trous):
    n1 = len(mot)
    n2 = len(mot_a_trous)
    if n1 != n2:
        return False
    for i in range(n1):
        if mot[i] != mot_a_trous[i] and mot_a_trous[i] != '*':
            return False
    return True
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert correspond('INFORMATIQUE', 'INFO*MA*IQUE')
assert not correspond('AUTOMATIQUE', 'INFO*MA*IQUE')
assert not correspond('STOP', 'S*')
assert correspond('AUTO', '*UT*')
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert correspond('INFORMATIQUE', 'INFO*MA*IQUE')
assert not correspond('AUTOMATIQUE', 'INFO*MA*IQUE')
assert not correspond('STOP', 'S*')
assert correspond('AUTO', '*UT*')
# --- PYODIDE:post --- #
##########################