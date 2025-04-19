def couples_consecutifs(tab):
    t = []
    for i in range(1, len(tab)):
        if tab[i-1] + 1 == tab[i]:
            t.append((tab[i-1], tab[i]))
    return t