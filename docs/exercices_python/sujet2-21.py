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

def renverse(pile):
    '''renvoie une pile contenant les mêmes éléments que pile,
    mais dans l'ordre inverse.
    Cette fonction détruit pile.'''
    pile_inverse = ... 
    while pile != []:
        ... .append(...) 
    return ... 


def positifs(pile):
    '''renvoie une pile contenant les éléments positifs de pile,
    dans le même ordre. Cette fonction détruit pile.'''
    pile_positifs = ... 
    while pile != []:
        ... = pile.pop() 
        if ... >= 0: 
            ...
    return ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def renverse(pile):
    '''renvoie une pile contenant les mêmes éléments que pile,
    mais dans l'ordre inverse.
    Cette fonction détruit pile.'''
    pile_inverse = [] 
    while pile != []:
        pile_inverse.append(pile.pop()) 
    return pile_inverse


def positifs(pile):
    '''renvoie une pile contenant les éléments positifs de pile,
    dans le même ordre. Cette fonction détruit pile.'''
    pile_positifs = []
    while pile != []:
        v = pile.pop() 
        if v >= 0:
            pile_positifs.append(v)
    return renverse(pile_positifs)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert renverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
assert positifs([-1, 0, 5, -3, 4, -6, 10, 9, -8]) == [0, 5, 4, 10, 9]
assert positifs([-2]) == []
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert renverse([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
assert positifs([-1, 0, 5, -3, 4, -6, 10, 9, -8]) == [0, 5, 4, 10, 9]
assert positifs([-2]) == []
# --- PYODIDE:post --- #
##########################