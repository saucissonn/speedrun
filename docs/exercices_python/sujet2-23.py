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

def nombre_suivant(s):
    '''Renvoie le nombre suivant de celui representé par s
    en appliquant le procédé de lecture.'''
    resultat = ''
    chiffre = s[0]
    compte = 1
    for i in range(...): 
        if s[i] == chiffre:
            compte = ... 
        else:
            resultat += ... + ... 
            chiffre = ... 
            ...
    lecture_... = ... + ... 
    resultat += lecture_chiffre
    return resultat

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0: 
        return str(r) 
    else:
        return dec_to_bin(q) + str(r)

def bin_to_dec(nb_bin):
    if len(nb_bin) == 1:
        if nb_bin == '0': 
            return 0
        else:
            return 1 
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert dec_to_bin(25) == '11001'
assert bin_to_dec('101010') == 42
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert dec_to_bin(25) == '11001'
assert bin_to_dec('101010') == 42
# --- PYODIDE:post --- #
##########################