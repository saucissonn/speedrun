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

def plus_ou_moins2():
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
import builtins
from io import StringIO
import sys

def plus_ou_moins2():
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

def test_equivalence_plus_ou_moins():
    # Sauvegarde l'ancien input et stdout
    old_input = builtins.input
    old_stdout = sys.stdout

    # Prépare les entrées simulées
    entrees = ["40", "60", "80", "90", "95", "97", "98", "99"]
    input_iter = iter(entrees)
    builtins.input = lambda _: next(input_iter)

    # Force le même nombre mystère
    from random import randint
    import random
    random.randint = lambda a, b: 99

    # Capture la sortie de plus_ou_moins2
    sys.stdout = StringIO()
    plus_ou_moins2()
    sortie2 = sys.stdout.getvalue()

    # Prépare à nouveau les entrées
    entrees = ["40", "60", "80", "90", "95", "97", "98", "99"]
    input_iter = iter(entrees)
    builtins.input = lambda _: next(input_iter)

    # Capture la sortie de plus_ou_moins
    sys.stdout = StringIO()
    plus_ou_moins()
    sortie1 = sys.stdout.getvalue()

    # Restaure input et stdout
    builtins.input = old_input
    sys.stdout = old_stdout

    # Compare les sorties
    assert sortie1 == sortie2, f"Différences détectées :\nplus_ou_moins:\n{sortie1}\nplus_ou_moins2:\n{sortie2}"
test_equivalence_plus_ou_moins()
# --- PYODIDE:post --- #
##########################