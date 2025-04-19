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

def ligne_suivante(ligne):
    '''Renvoie la ligne suivant ligne du triangle de Pascal'''
    ligne_suiv = [...] 
    for i in range(...): 
        ligne_suiv.append(...) 
    ligne_suiv.append(...) 
    return ligne_suiv

def pascal(n):
    '''Renvoie le triangle de Pascal de hauteur n'''
    triangle = [ [1] ]
    for k in range(...): 
        ligne_k = ... 
        triangle.append(ligne_k)
    return triangle

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def ligne_suivante(ligne):
    '''Renvoie la ligne suivant ligne du triangle de Pascal'''
    ligne_suiv = [1] 
    for i in range(1, len(ligne)): 
        ligne_suiv.append(ligne[i-1]+ligne[i]) 
    ligne_suiv.append(1) 
    return ligne_suiv

def pascal(n):
    '''Renvoie le triangle de Pascal de hauteur n'''
    triangle = [ [1] ]
    for k in range(1,n+1): 
        ligne_k =ligne_suivante(triangle[k-1])
        triangle.append(ligne_k)
    return triangle
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert pascal(2) == [[1], [1, 1], [1, 2, 1]]
assert pascal(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert pascal(2) == [[1], [1, 1], [1, 2, 1]]
assert pascal(3) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
# --- PYODIDE:post --- #
##########################