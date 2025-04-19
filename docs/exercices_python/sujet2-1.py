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

def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(...): 
        if s[i] == chiffre:
            compte = ... 
        else:
            resultat += ... + ... 
            chiffre = ... 
            ...
    lecture_... = ... + ... 
    resultat += lecture_chiffre
    return resultat

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(1, len(s)): 
        if s[i] == chiffre:
            compte = compte + 1 
        else:
            resultat += str(compte) + chiffre 
            chiffre = s[i] 
            compte = 1
    lecture_chiffre = str(compte) + chiffre 
    resultat += lecture_chiffre
    return resultat
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert nombre_suivant('1211') == '111221'
assert nombre_suivant('311') == '1321'
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert nombre_suivant('1211') == '111221'
assert nombre_suivant('311') == '1321'
# --- PYODIDE:post --- #
##########################