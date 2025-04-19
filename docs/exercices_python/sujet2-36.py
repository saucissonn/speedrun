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

class Noeud:
    def __init__(self, etiquette):
        '''Méthode constructeur pour la classe Noeud.
        Crée une feuille d'étiquette donnée.'''
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        '''Insère la clé dans l'arbre binaire de recherche
        en préservant sa structure.'''
        if cle < self.etiquette:
            if self.gauche != None:
                ...
            else:
                self.gauche = ... 
        else:
            ...
                ...
            else:
                ... = Noeud(cle) 

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
class Noeud:
    def __init__(self, etiquette):
        '''Méthode constructeur pour la classe Noeud.
        Crée une feuille d'étiquette donnée.'''
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        '''Insère la clé dans l'arbre binaire de recherche
        en préservant sa structure.'''
        if cle < self.etiquette:
            if self.gauche != None:
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle) 
        else:
            if self.droit != None:
                self.droit.inserer(cle)
            else:
                self.droit = Noeud(cle)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)
assert arbre.gauche.etiquette == 3
assert arbre.droit.etiquette == 9
assert arbre.gauche.gauche.etiquette == 1
assert arbre.gauche.droit.etiquette == 6
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)
assert arbre.gauche.etiquette == 3
assert arbre.droit.etiquette == 9
assert arbre.gauche.gauche.etiquette == 1
assert arbre.gauche.droit.etiquette == 6
# --- PYODIDE:post --- #
##########################