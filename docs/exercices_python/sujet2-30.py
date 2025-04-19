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

class Expr:
    """Classe implémentant un arbre d'expression."""

    def __init__(self, g, v, d):
        """un objet Expr possède 3 attributs :
        - gauche : la sous-expression gauche ;
        - valeur : la valeur de l'étiquette, opérateur ou nombre ;
        - droite : la sous-expression droite."""
        self.gauche = g
        self.valeur = v
        self.droite = d

    def est_une_feuille(self):
        """renvoie True si et seulement 
        si le noeud est une feuille"""
        return self.gauche is None and self.droite is None

    def infixe(self):
        """renvoie la représentation infixe de l'expression en
        chaine de caractères"""
        s = ... 
        if self.gauche is not None:
            s = s + '(' + ... .infixe() 
        s = s + ... 
        if ... is not None: 
            s = s + ... + ... 
        return s

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
class Expr:
    """Classe implémentant un arbre d'expression."""

    def __init__(self, g, v, d):
        """un objet Expr possède 3 attributs :
        - gauche : la sous-expression gauche ;
        - valeur : la valeur de l'étiquette, opérande ou nombre ;
        - droite : la sous-expression droite."""
        self.gauche = g
        self.valeur = v
        self.droite = d

    def est_une_feuille(self):
        """renvoie True si et seulement 
        si le noeud est une feuille"""
        return self.gauche is None and self.droite is None

    def infixe(self):
        """renvoie la représentation infixe de l'expression en
        chaine de caractères"""
        s = "" 
        if self.gauche is not None:
            s = '(' + s + self.gauche.infixe() 
        s = s + str(self.valeur) 
        if self.droite is not None: 
            s = s + self.droite.infixe() + ')' 
        return s
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
a = Expr(Expr(None, 1, None), '+', Expr(None, 2, None))
assert a.infixe() == '(1+2)'
b = Expr(Expr(Expr(None, 1, None), '+', Expr(None, 2, None)), '*', Expr(Expr(None, 3, None), '+', Expr(None, 4, None)))
assert b.infixe() == '((1+2)*(3+4))'
e = Expr(Expr(Expr(None, 3, None), '*', Expr(Expr(None, 8, None), '+', Expr(None, 7, None))), '-', Expr(Expr(None, 2, None), '+', Expr(None, 1, None)))
assert e.infixe() == '((3*(8+7))-(2+1))'
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
a = Expr(Expr(None, 1, None), '+', Expr(None, 2, None))
assert a.infixe() == '(1+2)'
b = Expr(Expr(Expr(None, 1, None), '+', Expr(None, 2, None)), '*', Expr(Expr(None, 3, None), '+', Expr(None, 4, None)))
assert b.infixe() == '((1+2)*(3+4))'
e = Expr(Expr(Expr(None, 3, None), '*', Expr(Expr(None, 8, None), '+', Expr(None, 7, None))), '-', Expr(Expr(None, 2, None), '+', Expr(None, 1, None)))
assert e.infixe() == '((3*(8+7))-(2+1))'
# --- PYODIDE:post --- #
##########################