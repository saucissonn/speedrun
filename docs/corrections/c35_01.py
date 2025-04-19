def max_dico(dico):
    lmax = 0
    nom = ""
    for k,v in dico.items():
        if v > lmax:
            lmax = v
            nom = k
    return (nom, lmax)