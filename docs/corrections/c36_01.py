def nombre_de_mots(phrase):
    n = len(phrase)
    cpt = 0
    for c in phrase:
        if c == ' ':
            cpt = cpt + 1
    if phrase[n-1] == '.':
        return cpt + 1
    else :
        return cpt