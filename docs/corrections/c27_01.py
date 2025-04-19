def verifie(tab):
    n = len(tab)
    if n < 2 :
        return True
    for i in range(1,n) :
        if tab[i] < tab[i-1] :
            return False
    return True