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

def empaqueter(liste_masses, c):
    """Renvoie le nombre minimal de boîtes nécessaires pour
    empaqueter les objets de la liste liste_masses, sachant
    que chaque boîte peut contenir au maximum c kilogrammes"""
    n = len(liste_masses)
    nb_boites = 0
    boites = [ 0 for _ in range(n) ]
    for masse in ...: 
        i = 0
        while i < nb_boites and boites[i] + ... > c: 
            i = i + 1
        if i == nb_boites:
            ...
        boites[i] = ... 
    return ... 

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def empaqueter(liste_masses, c):
    """Renvoie le nombre minimal de boîtes nécessaires pour
    empaqueter les objets de la liste liste_masses, sachant
    que chaque boîte peut contenir au maximum c kilogrammes"""
    n = len(liste_masses)
    nb_boites = 0
    boites = [ 0 for _ in range(n) ]
    for masse in liste_masses: 
        i = 0
        while i < nb_boites and boites[i] + masse > c: 
            i = i + 1
        if i == nb_boites:
            nb_boites = nb_boites + 1
        boites[i] = boites[i] + masse 
    return nb_boites
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert empaqueter([1, 2, 3, 4, 5], 10) == 2
assert empaqueter([1, 2, 3, 4, 5], 5) == 4
assert empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11) == 5
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert empaqueter([1, 2, 3, 4, 5], 10) == 2
assert empaqueter([1, 2, 3, 4, 5], 5) == 4
assert empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11) == 5
# --- PYODIDE:post --- #
##########################