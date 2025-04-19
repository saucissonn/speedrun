def moyenne (tab):
    s_coef = 0
    s_note = 0
    for t in tab:
        s_coef = s_coef + t[1]
        s_note = s_note + t[0]*t[1]
    if s_coef == 0:
        return None
    else :
        return s_note / s_coef
        