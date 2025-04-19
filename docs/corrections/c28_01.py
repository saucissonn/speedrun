def a_doublon(tab):
    for i in range(1, len(tab)):
        if tab[i-1] == tab[i]:
            return True
    return False