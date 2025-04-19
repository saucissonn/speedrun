import random
def lancer(n):
    tlancer = []
    for i in range(6):
        tlancer.append(random.randint(1,6))
    return tlancer

def paire_6(tab):
    cpt = 0
    for v in tab:
        if v == 6:
            cpt = cpt + 1
    return cpt >= 2

