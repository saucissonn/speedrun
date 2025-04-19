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

def recherche_motif(elt, lst):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def recherche_motif(motif, texte):
    t = []
    for i in range(len(texte) - len(motif) + 1):
        j = 0
        corr = True
        while  corr and j < len(motif):
            if texte[i+j] == motif[j]:
                j = j + 1
            else :
                corr = False 
        if corr:
            t.append(i)
    return t
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert recherche_motif("ab", "") == []
assert recherche_motif("ab", "cdcdcdcd") == []
assert recherche_motif("ab", "abracadabra") == [0, 7]
assert recherche_motif("ab", "abracadabraab") == [0, 7, 11]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert recherche_motif("ab", "") == []
assert recherche_motif("ab", "cdcdcdcd") == []
assert recherche_motif("ab", "abracadabra") == [0, 7]
assert recherche_motif("ab", "abracadabraab") == [0, 7, 11]
# --- PYODIDE:post --- #
##########################