def nbr_occurrences(chaine):
    d = {}
    for c in chaine:
        if c in d:
            d[c] = d[c] + 1
        else :
            d[c] = 1
    return d
