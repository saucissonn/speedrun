def inverse_chaine(chaine):
    '''Retourne la chaine inversée'''
    resultat = "" 
    for caractere in chaine:
        resultat = caractere + resultat 
    return resultat

def est_palindrome(chaine):
    '''Renvoie un booléen indiquant si la chaine ch
    est un palindrome'''
    inverse = inverse_chaine(chaine)
    return inverse == chaine 

def est_nbre_palindrome(nbre):
    '''Renvoie un booléen indiquant si le nombre nbre 
    est un palindrome'''
    chaine = str(nbre) 
    return est_palindrome(chaine)



