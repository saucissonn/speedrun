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

def depouille(urne):
    '''prend en paramètre une liste de suffrages et renvoie un 
    dictionnaire avec le nombre de voix pour chaque candidat'''
    resultat = ... 
    for bulletin in urne:
        if ...: 
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            ...
    return resultat

def vainqueurs(election):
    '''prend en paramètre un dictionnaire non vide avec le nombre de voix
    pour chaque candidat et renvoie la liste des vainqueurs'''
    nmax = 0
    for candidat in election:
        if ... > ... : 
            nmax = ... 
    liste_finale = [ nom for nom in election if ... ] 
    return ... 

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def depouille(urne):
    '''prend en paramètre une liste de suffrages et renvoie un 
    dictionnaire avec le nombre de voix pour chaque candidat'''
    resultat = {} 
    for bulletin in urne:
        if bulletin in resultat: 
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1
    return resultat

def vainqueurs(election):
    '''prend en paramètre un dictionnaire non vide avec le nombre de voix
    pour chaque candidat et renvoie la liste des vainqueurs'''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax : 
            nmax = election[candidat] 
    liste_finale = [ nom for nom in election if election[nom] == nmax ] 
    return liste_finale
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert depouille([ 'A', 'B', 'A' ]) == {'A': 2, 'B': 1}
assert depouille([]) == {}
election = depouille(['A', 'A', 'A', 'B', 'C', == 'B', 'C', 'B', 'C', 'B'])
assert election == {'A': 3, 'B': 4, 'C': 3}
assert vainqueurs(election) == ['B']
assert vainqueurs({ 'A' : 2, 'B' : 2, 'C' : 1}) == ['A', 'B']
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert depouille([ 'A', 'B', 'A' ]) == {'A': 2, 'B': 1}
assert depouille([]) == {}
election = depouille(['A', 'A', 'A', 'B', 'C', == 'B', 'C', 'B', 'C', 'B'])
assert election == {'A': 3, 'B': 4, 'C': 3}
assert vainqueurs(election) == ['B']
assert vainqueurs({ 'A' : 2, 'B' : 2, 'C' : 1}) == ['A', 'B']
# --- PYODIDE:post --- #
##########################