def nb_repetitions(elt, tab):
    cpt = 0
    for e in tab:
        if e == elt:
            cpt = cpt + 1
    return cpt