def multiplication(n1, n2):
    if n1 < 0 and n2 > 0 :
        return -multiplication(-n1, n2)
    if n1 > 0 and n2 < 0 :
        return -multiplication(n1, -n2)
    if n1 < 0 and n2 < 0 :
        return multiplication(-n1, -n2)
    s = 0
    for i in range(n1):
        s = s + n2
    return s