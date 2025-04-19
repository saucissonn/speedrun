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

def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == ...: 
        return ... 
    else:
        return dec_to_bin(...) + ... 

def bin_to_dec(nb_bin):
    if len(nb_bin) == 1:
        if ... == '0': 
            return 0
        else:
            return ... 
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            ...
        return ... * bin_to_dec(nb_bin[:-1]) + ... 

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
assert 1 == 1
# --- PYODIDE:post --- #
##########################