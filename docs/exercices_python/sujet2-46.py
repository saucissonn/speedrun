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

pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def rendu_monnaie(somme_due, somme_versee):
    '''Renvoie la liste des pièces à rendre pour rendre la monnaie
    lorsqu'on doit rendre somme_versee - somme_due'''
    rendu = ... 
    a_rendre = ... 
    i = len(pieces) - 1
    while a_rendre > ...: 
        while pieces[i] > a_rendre:
            i = i - 1
        rendu.append(...) 
        a_rendre = ... 
    return rendu

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def rendu_monnaie(somme_due, somme_versee):
    '''Renvoie la liste des pièces à rendre pour rendre la monnaie
    lorsqu'on doit rendre somme_versee - somme_due'''
    rendu = [] 
    a_rendre = somme_versee - somme_due
    i = len(pieces) - 1
    while a_rendre > 0: 
        while pieces[i] > a_rendre:
            i = i - 1
        rendu.append(pieces[i]) 
        a_rendre = a_rendre -pieces[i]
    return rendu
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert compte_occurrences('a', ['a','b','c','a','d','e','a']) == 3
assert rendu_monnaie(700, 700) == []
assert rendu_monnaie(102, 500) == [200, 100, 50, 20, 20, 5, 2, 1]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert compte_occurrences('a', ['a','b','c','a','d','e','a']) == 3
assert rendu_monnaie(700, 700) == []
assert rendu_monnaie(102, 500) == [200, 100, 50, 20, 20, 5, 2, 1]
# --- PYODIDE:post --- #
##########################