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

def nombre_de_mots(txt):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def nombre_de_mots(phrase):
    n = len(phrase)
    cpt = 0
    for c in phrase:
        if c == ' ':
            cpt = cpt + 1
    if phrase[n-1] == '.':
        return cpt + 1
    else :
        return cpt
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert nombre_de_mots('Cet exercice est simple.') == 4
assert nombre_de_mots('Le point d exclamation est séparé !') == 6
assert nombre_de_mots('Combien de mots y a t il dans cette phrase ?') == 10
assert nombre_de_mots('Fin.') == 1
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert nombre_de_mots('Cet exercice est simple.') == 4
assert nombre_de_mots('Le point d exclamation est séparé !') == 6
assert nombre_de_mots('Combien de mots y a t il dans cette phrase ?') == 10
assert nombre_de_mots('Fin.') == 1
# --- PYODIDE:post --- #
##########################