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

resultats = {
    'Dupont': {
        'DS1': [15.5, 4],
        'DM1': [14.5, 1],
        'DS2': [13, 4],
        'PROJET1': [16, 3],
        'DS3': [14, 4]
    },
    'Durand': {
        'DS1': [6 , 4],
        'DS2': [8, 4],
        'PROJET1': [9, 3],
        'IE1': [7, 2],
        'DS3': [12, 4]
    }
}

def moyenne(nom, resultats):
    '''Renvoie la moyenne de l'élève nom, selon le dictionnaire 
    resultats. Si nom n'est pas dans le dictionnaire, 
    la fonction renvoie None.'''
    if nom in ...: 
        notes = resultats[nom]
        if ...: # pas de notes 
            return 0
        total_points = ... 
        total_coefficients = ... 
        for ...  in notes.values(): 
            note, coefficient = valeurs
            total_points = total_points + ... * coefficient 
            ... = ... + coefficient 
        return round( ... / total_coefficients, 1 ) 
    else:
        return None

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
resultats = {
    'Dupont': {
        'DS1': [15.5, 4],
        'DM1': [14.5, 1],
        'DS2': [13, 4],
        'PROJET1': [16, 3],
        'DS3': [14, 4]
    },
    'Durand': {
        'DS1': [6 , 4],
        'DS2': [8, 4],
        'PROJET1': [9, 3],
        'IE1': [7, 2],
        'DS3': [12, 4]
    }
}

def moyenne(nom, resultats):
    '''Renvoie la moyenne de l'élève nom, selon le dictionnaire 
    resultats. Si nom n'est pas dans le dictionnaire, 
    la fonction renvoie None.'''
    if nom in resultats: 
        notes = resultats[nom]
        if len(notes) == 0: # pas de notes 
            return 0
        total_points = 0 
        total_coefficients = 0 
        for valeurs  in notes.values(): 
            note, coefficient = valeurs
            total_points = total_points + note * coefficient 
            total_coefficients = total_coefficients + coefficient 
        return round( total_points/ total_coefficients, 1 ) 
    else:
        return None
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert recherche_indices_classement(3, []) == ([], [], [])
assert moyenne("Dupont", resultats) == 14.5
assert moyenne("Durand", resultats) == 8.5
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert recherche_indices_classement(3, []) == ([], [], [])
assert moyenne("Dupont", resultats) == 14.5
assert moyenne("Durand", resultats) == 8.5
# --- PYODIDE:post --- #
##########################