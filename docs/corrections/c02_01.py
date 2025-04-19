def max_et_indice(tab):
    imax = 0
    vmax = tab[0]
    for i in range(len(tab)):
        if tab[i] > vmax:
            vmax = tab[i]
            imax = i
    return (vmax, imax)
