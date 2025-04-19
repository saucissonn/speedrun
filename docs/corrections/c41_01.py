def ou_exclusif(t1, t2):
    t = []
    for i in range(len(t1)):
        if t1[i] == t2[i]:
            t.append(0)
        else:
            t.append(1)
    return t