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

dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
        "W": 23, "X": 24, "Y": 25, "Z": 26}

def codes_parfait(mot):
    """Renvoie un triplet 
    (code_additionne, code_concatene, mot_est_parfait) où :
    - code_additionne est la somme des codes des lettres du mot ;
    - code_concatene est le code des lettres du mot concaténées ;
    - mot_est_parfait est un booléen indiquant si le mot est parfait."""
    code_concatene = ""
    code_additionne = ... 
    for c in mot:
        code_concatene = code_concatene + ... 
        code_additionne = code_additionne + ... 
    code_concatene = int(code_concatene)
    mot_est_parfait = ... 
    return code_additionne, code_concatene, mot_est_parfait

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
        "W": 23, "X": 24, "Y": 25, "Z": 26}

def codes_parfait(mot):
    """Renvoie un triplet 
    (code_additionne, code_concatene, mot_est_parfait) où :
    - code_additionne est la somme des codes des lettres du mot ;
    - code_concatene est le code des lettres du mot concaténées ;
    - mot_est_parfait est un booléen indiquant si le mot est parfait."""
    code_concatene = ""
    code_additionne = 0 
    for c in mot:
        code_concatene = code_concatene + str(dico[c]) 
        code_additionne = code_additionne + dico[c]
    code_concatene = int(code_concatene)
    mot_est_parfait = (code_concatene % code_additionne) == 0 
    return code_additionne, code_concatene, mot_est_parfait
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert liste_puissances_borne(2, 17) == [2, 4, 8, 16]
assert liste_puissances_borne(5, 5) == []
assert codes_parfait("PAUL") == (50, 1612112, False)
assert codes_parfait("ALAIN") == (37, 1121914, True)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert liste_puissances_borne(2, 17) == [2, 4, 8, 16]
assert liste_puissances_borne(5, 5) == []
assert codes_parfait("PAUL") == (50, 1612112, False)
assert codes_parfait("ALAIN") == (37, 1121914, True)
# --- PYODIDE:post --- #
##########################