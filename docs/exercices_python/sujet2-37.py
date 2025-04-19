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

def tri_insertion(tab):
    '''Trie le tableau tab par ordre croissant
    en appliquant l'algorithme de tri par insertion'''
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = ... 
        # la variable j sert à déterminer 
        # où placer la valeur à ranger
        j = ... 
        # tant qu'on n'a pas trouvé la place de l'élément à
        # insérer on décale les valeurs du tableau vers la droite
        while j > ... and valeur_insertion < tab[...]: 
            tab[j] = tab[j-1]
            j = ... 
        tab[j] = ... 

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def tri_insertion(tab):
    '''Trie le tableau tab par ordre croissant
    en appliquant l'algorithme de tri par insertion'''
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i] 
        # la variable j sert à déterminer 
        # où placer la valeur à ranger
        j = i 
        # tant qu'on n'a pas trouvé la place de l'élément à
        # insérer on décale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j-1]: 
            tab[j] = tab[j-1]
            j = j - 1 
        tab[j] = valeur_insertion
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
tab = [98, 12, 104, 23, 131, 9]
tri_insertion(tab)
assert tab == [9, 12, 23, 98, 104, 131]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
tab = [98, 12, 104, 23, 131, 9]
tri_insertion(tab)
assert tab == [9, 12, 23, 98, 104, 131]
# --- PYODIDE:post --- #
##########################