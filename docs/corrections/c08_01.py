def maximum_tableau(tab):
    vmax = tab[0]
    for v in tab:
        if v > vmax:
            vmax = v
    return vmax