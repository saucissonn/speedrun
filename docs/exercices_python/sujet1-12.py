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

def fusion(l1, l2):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def fusion(tab1, tab2):
    tab = []
    n1 = len(tab1)
    n2 = len(tab2)
    i = 0
    j = 0
    while i < n1 and j < n2 :
        if tab1[i] > tab2[j]:
            tab.append(tab2[j])
            j = j + 1
        else :
            tab.append(tab1[i])
            i = i + 1
    while i < n1 :
        tab.append(tab1[i])
        i = i + 1
    while j < n2 :
        tab.append(tab2[j])
        j = j + 1
    return tab
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert fusion([3, 5], [2, 5]) == [2, 3, 5, 5]
assert fusion([-2, 4], [-3, 5, 10]) == [-3, -2, 4, 5, 10]
assert fusion([4], [2, 6]) == [2, 4, 6]
assert fusion([1, 2, 3], []) == [1, 2, 3]
assert fusion([], []) == []
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert fusion([3, 5], [2, 5]) == [2, 3, 5, 5]
assert fusion([-2, 4], [-3, 5, 10]) == [-3, -2, 4, 5, 10]
assert fusion([4], [2, 6]) == [2, 4, 6]
assert fusion([1, 2, 3], []) == [1, 2, 3]
assert fusion([], []) == []
# --- PYODIDE:post --- #
##########################