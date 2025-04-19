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

n0 = (None, 0, None)
n3 = (None, 3, None)
n2 = (None, 2, n3)
abr1 = (n0, 1, n2)

def insertion_abr(a, cle):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def insertion_abr(a,cle):
    if a == None:
        return (None, cle, None)
    if cle == a[1]:
        return a
    elif cle > a[1] :
        return  (a[0], a[1], insertion_abr(a[2], cle))
    else :
        return  (insertion_abr(a[0], cle), a[1], a[2])

n0 = (None, 0, None)
n3 = (None, 3, None)
n2 = (None, 2, n3)
abr1 = (n0, 1, n2)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert insertion_abr(abr1, 4) == ((None,0,None),1,(None,2,(None,3,(None,4,None))))
assert insertion_abr(abr1, -5) == (((None,-5,None),0,None),1,(None,2,(None,3,None)))
assert insertion_abr(abr1, 2) == ((None,0,None),1,(None,2,(None,3,None)))
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert insertion_abr(abr1, 4) == ((None,0,None),1,(None,2,(None,3,(None,4,None))))
assert insertion_abr(abr1, -5) == (((None,-5,None),0,None),1,(None,2,(None,3,None)))
assert insertion_abr(abr1, 2) == ((None,0,None),1,(None,2,(None,3,None)))
# --- PYODIDE:post --- #
##########################