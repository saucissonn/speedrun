def parcours_largeur(arb):
    file = [arb]
    t = []
    while len(file) != 0:
        x = file.pop(0)
        t.append(x[1])
        if x[0] != None:
            file.append(x[0])
        if x[2] != None:
            file.append(x[2])
    return t
