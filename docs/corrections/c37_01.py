def gb_vers_entier(tab):
    s = 0
    n = len(tab)
    for i in range(n):
        v = tab[n - 1 - i]
        if v :
            s = s + 2**i
    return s
        
        
