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

class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit

a = Noeud(1, Noeud(4, None, None), Noeud(0, None, Noeud(7, None, None)))

def taille(ABR):
    ...

def hauteur(ABR):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit

a = Noeud(1, Noeud(4, None, None), Noeud(0, None, Noeud(7, None, None)))

def taille(a):
    if a == None:
        return 0
    return 1 + taille(a.gauche) + taille(a.droit)

def hauteur(a):
    if a == None:
        return -1
    return 1 + max(hauteur(a.gauche), hauteur(a.droit))
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert hauteur(a) == 2
assert taille(a) == 4
assert hauteur(None) == -1
assert taille(None) == 0
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert hauteur(a) == 2
assert taille(a) == 4
assert hauteur(None) == -1
assert taille(None) == 0
# --- PYODIDE:post --- #
##########################