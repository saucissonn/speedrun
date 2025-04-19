def selection_enclos(animaux, num_enclos):
    t = []
    for d in animaux:
        if d['enclos'] == num_enclos:
            t.append(d)
    return t
