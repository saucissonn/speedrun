def occurrences(caractere, chaine):
    cpt = 0
    for c in chaine:
        if c == caractere :
            cpt = cpt + 1
    return cpt