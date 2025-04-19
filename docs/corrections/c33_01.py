def insertion_abr(a,cle):
    if a == None:
        return (None, cle, None)
    if cle == a[1]:
        return a
    elif cle > a[1] :
        return  (a[0], a[1], insertion_abr(a[2], cle))
    else :
        return  (insertion_abr(a[0], cle), a[1], a[2])

n0 = (None, 0, None)
n3 = (None, 3, None)
n2 = (None, 2, n3)
abr1 = (n0, 1, n2)