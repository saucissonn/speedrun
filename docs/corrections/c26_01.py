def ajoute_dictionnaires(d1, d2):
    d = {}
    for k in d1:
        if k in d2 :
            d[k] = d1[k] + d2[k]
        else :
            d[k] = d1[k]
    for k in d2:
        if k not in d:
            d[k] = d2[k]
    return d