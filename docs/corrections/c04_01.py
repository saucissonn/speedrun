def ecriture_binaire_entier_positif(n):
    vbin = str(n%2)
    n = n // 2
    while n > 0:
        vbin = str(n%2) + vbin
        n = n //2
    return vbin