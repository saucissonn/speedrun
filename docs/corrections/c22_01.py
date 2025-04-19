def recherche(elt, tab):
    res = None
    for i in range(len(tab)):
        if tab[i] == elt:
            res = i
    return res