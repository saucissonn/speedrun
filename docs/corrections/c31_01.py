def recherche_motif(motif, texte):
    t = []
    for i in range(len(texte) - len(motif) + 1):
        j = 0
        corr = True
        while  corr and j < len(motif):
            if texte[i+j] == motif[j]:
                j = j + 1
            else :
                corr = False 
        if corr:
            t.append(i)
    return t
        