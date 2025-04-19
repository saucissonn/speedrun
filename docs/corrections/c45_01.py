def correspond(mot, mot_a_trous):
    n1 = len(mot)
    n2 = len(mot_a_trous)
    if n1 != n2:
        return False
    for i in range(n1):
        if mot[i] != mot_a_trous[i] and mot_a_trous[i] != '*':
            return False
    return True