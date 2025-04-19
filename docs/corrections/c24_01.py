def enumere(tab):
    d = {}
    for i in range(len(tab)):
        if tab[i] not in d:
            d[tab[i]] = [i]
        else :
            d[tab[i]].append(i)
    return d