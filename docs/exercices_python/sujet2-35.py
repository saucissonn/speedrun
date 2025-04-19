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

class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie un booléen indiquant si la pile est vide."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'élément placé au sommet de la pile,
        si la pile n’est pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()

def eval_expression(tab):
    p = Pile()
    for ... in tab: 
        if element != '+' ... element != '*': 
            p.empiler(...) 
        else:
            if element == ...: 
                resultat = ... + ... 
            else:
                resultat = ... 
            p.empiler(...) 
    return ... 

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie un booléen indiquant si la pile est vide."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l'élément placé au sommet de la pile,
        si la pile n’est pas vide. Produit une erreur sinon.
        """
        assert not self.est_vide()
        return self.contenu.pop()

def eval_expression(tab):
    p = Pile()
    for element in tab: 
        if element != '+' and element != '*': 
            p.empiler(element) 
        else:
            if element == '+': 
                resultat = p.depiler() + p.depiler() 
            else:
                resultat = p.depiler() * p.depiler()  
            p.empiler(resultat) 
    return  p.depiler()
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert eval_expression([2, 3, '+', 5, '*']) == 25
assert eval_expression([1, 2, '+', 3, '*']) == 9
assert eval_expression([1, 2, 3, '+', '*']) == 5
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert eval_expression([2, 3, '+', 5, '*']) == 25
assert eval_expression([1, 2, '+', 3, '*']) == 9
assert eval_expression([1, 2, 3, '+', '*']) == 5
# --- PYODIDE:post --- #
##########################