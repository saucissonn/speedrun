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
    """Classe représentant un noeud d'un arbre binaire"""
    def __init__(self, etiquette, gauche, droit):
        """Crée un noeud de valeur etiquette avec 
        gauche et droit comme fils."""
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit

def parcours(arbre, liste):
    """parcours récursivement l'arbre en ajoutant les étiquettes
    de ses noeuds à la liste passée en argument en ordre infixe."""
    if arbre != None:
        parcours(arbre.gauche, liste)
        liste.append(arbre.etiquette)
        parcours(arbre.droit, liste)
    return liste

def insere(arbre, cle):
    """insere la cle dans l'arbre binaire de recherche
    représenté par arbre.
    Retourne l'arbre modifié."""
    if arbre == None:
        return Noeud(cle, None, None) # creation d'une feuille
    else:
        if ...: 
            arbre.gauche = insere(arbre.gauche, cle)
        else:
            arbre.droit = ... 
        return arbre

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
class Noeud:
    """Classe reprÃ©sentant un noeud d'un arbre binaire"""
    def __init__(self, etiquette, gauche, droit):
        """CrÃ©e un noeud de valeur etiquette avec 
        gauche et droit comme fils."""
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit

def parcours(arbre, liste):
    """parcours rÃ©cursivement l'arbre en ajoutant les Ã©tiquettes
    de ses noeuds Ã  la liste passÃ©e en argument en ordre infixe."""
    if arbre != None:
        parcours(arbre.gauche, liste)
        liste.append(arbre.etiquette)
        parcours(arbre.droit, liste)
    return liste

def insere(arbre, cle):
    """insere la cle dans l'arbre binaire de recherche
    reprÃ©sentÃ© par arbre.
    Retourne l'arbre modifiÃ©."""
    if arbre == None:
        return Noeud(cle, None, None) # creation d'une feuille
    else:
        if cle < arbre.etiquette: 
            arbre.gauche = insere(arbre.gauche, cle)
        else:
            arbre.droit = insere(arbre.droit, cle) 
        return arbre


a_5 = Noeud(5,None, None)
a_2 = insere(a_5,2)
a_7 = insere(a_2,7)
a_3 = insere(a_7,3)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert 1 == 1
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
a_5 = Noeud(5,None, None)
a_2 = insere(a_5,2)
a_7 = insere(a_2,7)
a_3 = insere(a_7,3)
a_1 = insere(a_3,1)
a_4 = insere(a_1,4)
a_6 = insere(a_4,6)
a_8 = insere(a_6,8)
l = []
assert parcours(a_5, l) == [1,2,3,4,5,6,7,8]
# --- PYODIDE:post --- #
##########################