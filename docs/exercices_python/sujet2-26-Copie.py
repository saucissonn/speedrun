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

from random import randint

def nombre_coups():
    '''Simule un jeu de plateau avec 12 cases et renvoie le nombre
    nécessaire de coups pour visiter toutes les cases.'''
    nombre_cases = 12
    # indique si une case a été vue
    cases_vues = [ False ] * nombre_cases
    nombre_cases_vues = 1
    cases_vues[0] = True
    case_en_cours = 0
    n = ... 
    while ... < ...: 
        x = randint(1, 6)
        case_en_cours = (case_en_cours + ...) % ... 
        if ...: 
            cases_vues[case_en_cours] = True
            nombre_cases_vues = ... 
        n = ... 
    return n

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
from random import randint

def nb_coups():
    '''Simule un jeu de plateau avec 12 cases et renvoie le nombre
    minimal de coups pour visiter toutes les cases.'''
    nombre_cases = 12
    # indique si une case a été vue
    cases_vues = [ False ] * nombre_cases
    nombre_cases_vues = 1
    cases_vues[0] = True
    case_en_cours = 0
    n = 0 
    while nombre_cases_vues < nombre_cases: 
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % nombre_cases
        if not  cases_vues[case_en_cours]: 
            cases_vues[case_en_cours] = True
            nombre_cases_vues = nombre_cases_vues + 1 
        n = n + 1 
    return n
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert 1 == 1
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert 1 == 1
# --- PYODIDE:post --- #
##########################