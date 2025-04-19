def recherche(tab, n):
    ind = None
    for i in range(len(tab)):
        if tab[i] == n:
            ind = i
    return ind