def effectif_notes(notes_eval):
    t = [0]*11
    for note in notes_eval:
        t[note] = t[note] + 1
    return t

def notes_triees(eff):
    t = []
    for i in range(len(eff)):
        for _ in range(eff[i]):
            t.append(i)
    return t


