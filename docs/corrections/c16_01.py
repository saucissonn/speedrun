def moyenne(notes):
    s = 0
    coef = 0
    for c in notes:
        s = s + c[0]*c[1]
        coef = coef + c[1]
    return s / coef