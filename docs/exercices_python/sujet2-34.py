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


from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, ...) 
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = ... 

    while nb_mystere != ... and compteur < ...: 
        compteur = compteur + 1
        if nb_mystere ... nb_test: 
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ", ...) 
        print("Nombre d'essais: ", ...) 
    else:
        print ("Perdu ! Le nombre était ", ...) 
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
from random import randint

def plus_ou_moins():
    nb_mystere = randint(1, 99) 
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1 

    while nb_mystere != nb_test and compteur < 10: 
        compteur = compteur + 1
        if nb_mystere > nb_test: 
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ", nb_mystere) 
        print("Nombre d'essais: ", compteur) 
    else:
        print ("Perdu ! Le nombre était ", nb_mystere)
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert 1 == 1
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert 1 == 1
# --- PYODIDE:post --- #
##########################