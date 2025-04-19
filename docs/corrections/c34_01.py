def tri_selection(tab):
    N = len(tab)
    for i in range(N-1):
        imin = i
        for j in range (i+1,N):
            if tab[j] < tab[imin]:
                imin = j
        if imin != i:
            tab[i], tab[imin] = tab[imin], tab[i]
            