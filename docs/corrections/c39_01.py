def moyenne(tab):
    N = len(tab)
    assert N != 0, "le tableau ne doit pas être vide"
    s = 0
    for v in tab:
        s = s + v
    return s / N