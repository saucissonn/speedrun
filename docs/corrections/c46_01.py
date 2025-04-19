def compte_occurrences(x, tab):
    cpt = 0
    for v in tab:
        if v == x:
            cpt = cpt + 1
    return cpt