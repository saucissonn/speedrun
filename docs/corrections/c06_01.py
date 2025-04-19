def liste_puissances(a,n):
    t = [a]
    for i in range(1, n):
        t.append(a*t[i-1])
    return t

def liste_puissances_borne(a, borne):
    if a >= borne:
        return []
    t = [a]
    i = 1
    while a*t[i-1] < borne:
        t.append(a*t[i-1])
        i = i + 1
    return t