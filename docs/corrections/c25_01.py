def annee_temperature_minimale(t_moy, annees):
    tmin = t_moy[0]
    an = annees[0]
    for i in range(1, len(t_moy)):
        if t_moy[i] < tmin :
            tmin = t_moy[i]
            an = annees[i]
    return (tmin, an)
