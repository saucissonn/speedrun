# --- PYODIDE:ignore --- #
##########################
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

def est_pair(n):
    ...



# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #

def est_pair(n):
    return not n%2



# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #

assert est_pair(3) is False
assert est_pair(24) is True



# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #

def tests():
    for n in range(100):
        val = est_pair(n)
        exp = n%2 == 0

        msg = f"est_pair({n})"                           # Minimum vital
        msg = f"est_pair({n}): valeur renvoyée {val}"    # Conseillé
        msg = f"est_pair({n}): {val} devrait être {exp}" # La totale

        assert val == exp, msg

tests()         # Ne pas oublier d'appeler la fonction de tests... ! x)
del tests       # Si vous ne voulez pas laisser de traces...


# --- PYODIDE:post --- #
##########################