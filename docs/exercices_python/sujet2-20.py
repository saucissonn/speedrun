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

class Carte:
    def __init__(self, c, v):
        """Initialise les attributs couleur (entre 1 et 4), 
        et valeur (entre 1 et 13). """
        self.couleur = c
        self.valeur = v

    def recuperer_valeur(self):
        """ Renvoie la valeur de la carte : 
        As, 2, ..., 10, Valet, Dame, Roi """
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', 
                   '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]

    def recuperer_couleur(self):
        """ Renvoie la couleur de la carte 
        (parmi pique, coeur, carreau, trèfle). """
        couleurs = ['pique', 'coeur', 'carreau', 'trèfle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        """ Initialise l'attribut contenu avec une liste des 52
        objets Carte possibles rangés par valeurs croissantes en
        commençant par pique, puis cœur, carreau et trèfle. """
        ...
        ...
            ...
                ...

    def recuperer_carte(self, pos):
        """ Renvoie la carte qui se trouve à la position pos 
        (entier compris entre 0 et 51). """
        ...
        ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
class Carte:
    def __init__(self, c, v):
        """Initialise les attributs couleur (entre 1 et 4), 
        et valeur (entre 1 et 13). """
        self.couleur = c
        self.valeur = v

    def recuperer_valeur(self):
        """ Renvoie la valeur de la carte : 
        As, 2, ..., 10, Valet, Dame, Roi """
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', 
                   '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]

    def recuperer_couleur(self):
        """ Renvoie la couleur de la carte 
        (parmi pique, coeur, carreau, trèfle). """
        couleurs = ['pique', 'coeur', 'carreau', 'trèfle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        """ Initialise l'attribut contenu avec une liste des 52
        objets Carte possibles rangés par valeurs croissantes en
        commençant par pique, puis coeur, carreau et tréfle. """
        self.contenu = []
        for c in range(1, 5):
            for v in range(1, 14):
                self.contenu.append(Carte(c, v))

    def recuperer_carte(self, pos):
        """ Renvoie la carte qui se trouve à la position pos 
        (entier compris entre 0 et 51). """
        assert pos > -1 and pos < 52, 'paramètre pos invalide'
        return self.contenu[pos]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
jeu = Paquet_de_cartes()
carte1 = jeu.recuperer_carte(20)
assert carte1.recuperer_valeur() + " de " + carte1.recuperer_couleur() == "8 de coeur"
carte2 = jeu.recuperer_carte(0)
assert carte2.recuperer_valeur() + " de " + carte2.recuperer_couleur() == "As de pique"
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
jeu = Paquet_de_cartes()
carte1 = jeu.recuperer_carte(20)
assert carte1.recuperer_valeur() + " de " + carte1.recuperer_couleur() == "8 de coeur"
carte2 = jeu.recuperer_carte(0)
assert carte2.recuperer_valeur() + " de " + carte2.recuperer_couleur() == "As de pique"
# --- PYODIDE:post --- #
##########################