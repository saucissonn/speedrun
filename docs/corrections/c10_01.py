def recherche(tab, n):
    i = 0
    j = len(tab)-1
    while j >= i :
        mil = (i+j)//2
        if tab[mil] == n:
            return mil
        elif tab[mil] > n:
            j = mil - 1
        else :
            i = mil + 1
    return None



# la version récursive est aussi possible :

def recherche_rec(tab, n):
    def search(tab, n, i, j):
        if j < i :
            return None
        mil = (i + j) // 2
        if tab[mil] == n :
            return mil
        elif tab[mil] > n :
            return search(tab, n, i, mil-1)
        else :
            return search(tab, n, mil+1, j)
    return search(tab,n, 0, len(tab)-1)
        