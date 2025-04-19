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

def binaire(a):
    '''convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return ... 
    bin_a = ... 
    while ... : 
        bin_a = ... + bin_a 
        a = ... 
    return bin_a

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def binaire(a):
    '''convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return "0" 
    bin_a = "" 
    while a > 0 : 
        bin_a = str(a % 2) + bin_a 
        a = a // 2 
    return bin_a
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert binaire(6) == '110'
assert binaire(127) == '1111111'
assert binaire(0) == '0'
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert binaire(6) == '110'
assert binaire(127) == '1111111'
assert binaire(0) == '0'
# --- PYODIDE:post --- #
##########################