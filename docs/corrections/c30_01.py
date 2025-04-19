def delta(liste):
    t = [liste[0]]
    for i in range(1, len(liste)):
        t.append(liste[i] - liste[i-1])
    return t
    