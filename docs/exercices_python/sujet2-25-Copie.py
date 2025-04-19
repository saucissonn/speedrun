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

def inverse_chaine(chaine):
    '''Retourne la chaine inversée'''
    resultat = ... 
    for caractere in chaine:
        resultat = ... 
    return resultat

def est_palindrome(chaine):
    '''Renvoie un booléen indiquant si la chaine ch
    est un palindrome'''
    inverse = inverse_chaine(chaine)
    return ... 

def est_nbre_palindrome(nbre):
    '''Renvoie un booléen indiquant si le nombre nbre 
    est un palindrome'''
    chaine = ... 
    return est_palindrome(chaine)

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def inverse_chaine(chaine):
    '''Retourne la chaine inversée'''
    resultat = "" 
    for caractere in chaine:
        resultat = caractere + resultat 
    return resultat

def est_palindrome(chaine):
    '''Renvoie un booléen indiquant si la chaine ch
    est un palindrome'''
    inverse = inverse_chaine(chaine)
    return inverse == chaine 

def est_nbre_palindrome(nbre):
    '''Renvoie un booléen indiquant si le nombre nbre 
    est un palindrome'''
    chaine = str(nbre) 
    return est_palindrome(chaine)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert inverse_chaine('bac') == 'cab'
assert not est_palindrome('NSI')
assert est_palindrome('ISN-NSI')
assert not est_nbre_palindrome(214312)
assert est_nbre_palindrome(213312)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert inverse_chaine('bac') == 'cab'
assert not est_palindrome('NSI')
assert est_palindrome('ISN-NSI')
assert not est_nbre_palindrome(214312)
assert est_nbre_palindrome(213312)
# --- PYODIDE:post --- #
##########################