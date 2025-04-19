def recherche_indices_classement(elt, tab):
    t_inf = []
    t_eq = []
    t_sup = []
    for i in range(len(tab)):
        if tab[i] == elt:
            t_eq.append(i)
        elif tab[i] < elt:
            t_inf.append(i)
        elif tab[i] > elt:
            t_sup.append(i)
    return (t_inf, t_eq, t_sup)