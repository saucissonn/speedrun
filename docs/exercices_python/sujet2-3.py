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

def eleves_du_mois(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = ... 

    for i in range(...): 
        if notes[i] == ...: 
            meilleurs_eleves.append(...) 
        elif notes[i] > note_maxi:
            note_maxi = ... 
            meilleurs_eleves = [...] 

    return (note_maxi, meilleurs_eleves)

eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def eleves_du_mois(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = [] 

    for i in range(len(eleves)): 
        if notes[i] == note_maxi: 
            meilleurs_eleves.append(eleves[i]) 
        elif notes[i] > note_maxi:
            note_maxi = notes[i] 
            meilleurs_eleves = [eleves[i]] 

    return (note_maxi, meilleurs_eleves)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert fibonacci(25) == 75025
assert eleves_du_mois(eleves_nsi, notes_nsi) == (80, ['c', 'f', 'h'])
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert fibonacci(25) == 75025
assert eleves_du_mois(eleves_nsi, notes_nsi) == (80, ['c', 'f', 'h'])
# --- PYODIDE:post --- #
##########################