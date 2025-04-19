def recherche_min(tab):
    vmin = tab[0]
    imin = 0
    for i in range(1, len(tab)):
        if tab[i] < vmin:
            vmin = tab[i]
            imin = i
    return imin