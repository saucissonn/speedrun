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

t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

def annee_temperature_minimale(t, a):
    ...

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def annee_temperature_minimale(t_moy, annees):
    tmin = t_moy[0]
    an = annees[0]
    for i in range(1, len(t_moy)):
        if t_moy[i] < tmin :
            tmin = t_moy[i]
            an = annees[i]
    return (tmin, an)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert annee_temperature_minimale(t_moy, annees) == (12.5, 2016)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert annee_temperature_minimale(t_moy, annees) == (12.5, 2016)
# --- PYODIDE:post --- #
##########################