def indices_maxi(tab):
    nmax = tab[0]
    tindice = [0]
    for i in range(1, len(tab)) :
        if tab[i] > nmax :
            nmax = tab[i]
            tindice = [i]
        elif tab[i] == nmax :
            tindice.append(i)
    return (nmax, tindice)
    