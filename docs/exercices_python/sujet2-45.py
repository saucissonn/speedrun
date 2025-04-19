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

def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire 'plan' correspondant à 
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et 
    False sinon.'''
    expediteur = 'A'
    destinataire = plan[...] 
    nb_destinataires = 1

    while destinataire != expediteur:
        destinataire = ... 
        nb_destinataires = ... 

    return nb_destinataires == ... 

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire `plan` correspondant à 
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et 
    False sinon.'''
    expediteur = 'A'
    destinataire = plan[expediteur] 
    nb_destinataires = 1

    while destinataire != expediteur:
        destinataire = plan[destinataire] 
        nb_destinataires = nb_destinataires + 1 

    return nb_destinataires == len(plan)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert not est_cyclique({'A':'E','F':'A','C':'D','E':'B','B':'F','D':'C'})
assert est_cyclique({'A':'E','F':'C','C':'D','E':'B','B':'F','D':'A'})
assert est_cyclique({'A':'B','F':'C','C':'D','E':'A','B':'F','D':'E'})
assert not est_cyclique({'A':'B','F':'A','C':'D','E':'C','B':'F','D':'E'})
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert not est_cyclique({'A':'E','F':'A','C':'D','E':'B','B':'F','D':'C'})
assert est_cyclique({'A':'E','F':'C','C':'D','E':'B','B':'F','D':'A'})
assert est_cyclique({'A':'B','F':'C','C':'D','E':'A','B':'F','D':'E'})
assert not est_cyclique({'A':'B','F':'A','C':'D','E':'C','B':'F','D':'E'})
# --- PYODIDE:post --- #
##########################