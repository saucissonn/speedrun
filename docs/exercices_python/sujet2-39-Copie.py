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

def tri(tab):
    '''tab est un tableau d'entiers contenant des 0 et des 1.
    La fonction trie ce tableau en plaçant tous les 0 à gauche'''
    i = ... # premier indice de la zone non triée 
    j = ... # dernier indice de la zone non triée 
    while i < j:
        if tab[i] == 0:
            i = ... 
        else:
            valeur = ... 
            tab[j] = ... 
            ...
            j = ... 

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def tri(tab):
    '''tab est un tableau d'entiers contenant des 0 et des 1.
    La fonction trie ce tableau en plaçant tous les 0 à gauche'''
    i = 0 # premier indice de la zone non triée 
    j = len(tab) - 1 # dernier indice de la zone non triée 
    while i < j:
        if tab[i]== 0:
            i = i + 1 
        else:
            valeur = tab[j] 
            tab[j] = 1 
            tab[i] = valeur
            j = j - 1
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
tab = [0,1,0,1,0,1,0,1,0]
tri(tab)
assert tab == [0, 0, 0, 0, 0, 1, 1, 1, 1]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
tab = [0,1,0,1,0,1,0,1,0]
tri(tab)
assert tab == [0, 0, 0, 0, 0, 1, 1, 1, 1]
# --- PYODIDE:post --- #
##########################