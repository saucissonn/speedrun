def fusion(tab1, tab2):
    tab = []
    n1 = len(tab1)
    n2 = len(tab2)
    i = 0
    j = 0
    while i < n1 and j < n2 :
        if tab1[i] > tab2[j]:
            tab.append(tab2[j])
            j = j + 1
        else :
            tab.append(tab1[i])
            i = i + 1
    while i < n1 :
        tab.append(tab1[i])
        i = i + 1
    while j < n2 :
        tab.append(tab2[j])
        j = j + 1
    return tab