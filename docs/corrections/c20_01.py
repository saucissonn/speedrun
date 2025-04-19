def min_et_max(tab):
    vmin = tab[0]
    vmax = tab[0]
    for v in tab:
        if v > vmax:
            vmax = v
        if v < vmin:
            vmin = v
    return {"min":vmin, "max":vmax}
    