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

def fusion(tab1,tab2):
    '''Fusionne deux tableaux triés et renvoie
    le nouveau tableau trié.'''
    n1 = len(tab1)
    n2 = len(tab2)
    tab12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and ...: 
        if tab1[i1] < tab2[i2]:
            tab12[i] = ... 
            i1 = ... 
        else:
            tab12[i] = tab2[i2]
            i2 = ... 
        i += 1
    while i1 < n1:
        tab12[i] = ... 
        i1 = i1 + 1
        i = ... 
    while i2 < n2:
        tab12[i] = ... 
        i2 = i2 + 1
        i = ... 
    return tab12

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def fusion(tab1,tab2):
    '''Fusionne deux tableaux triés et renvoie
    le nouveau tableau trié.'''
    n1 = len(tab1)
    n2 = len(tab2)
    tab12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2: 
        if tab1[i1] < tab2[i2]:
            tab12[i] = tab1[i1]
            i1 = i1 + 1 
        else:
            tab12[i] = tab2[i2]
            i2 = i2 + 1 
        i += 1
    while i1 < n1:
        tab12[i] = tab1[i1] 
        i1 = i1 + 1
        i = i + 1 
    while i2 < n2:
        tab12[i] = tab2[i2] 
        i2 = i2 + 1
        i = i + 1 
    return tab12
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert fusion([], []) == []
assert fusion([1, 6, 10],[0, 7, 8, 9]) == [0, 1, 6, 7, 8, 9, 10]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert fusion([], []) == []
assert fusion([1, 6, 10],[0, 7, 8, 9]) == [0, 1, 6, 7, 8, 9, 10]
# --- PYODIDE:post --- #
##########################