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

def fibonacci(n):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def fibonacci(n):
    if n < 2 :
        return n
    return fibonacci(n-1) + fibonacci(n-2)

#utilisation de la prog dynamique (ascendante)
def fibonaccib(n):
    t = [0]*(n+1)
    t[1] = 1
    for i in range(2, n+1):
        t[i] = t[i-1] + t[i-2]
    return t[n]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert fibonacci(1) == 1
assert fibonacci(2) == 1
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert fibonacci(1) == 1
assert fibonacci(2) == 1
# --- PYODIDE:post --- #
##########################