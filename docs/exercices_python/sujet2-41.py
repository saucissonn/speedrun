# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:env --- #
class Stack:
    """ (Interface à décrire dans l'énoncé) """
    def __init__(self): self.__stk=[]
    def push(self, v): self.__stk.append(v)
    def pop(self): return self.__stk.pop()
    def is_empty(self): return not self.__stk
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:code --- #

class Carre:
    def __init__(self, liste, n): 
        self.ordre = n        
        self.tableau = [[liste[i + j * n] for i in range(n)] 
                        for j in range(n)] 
                                   
    def affiche(self):        
        '''Affiche un carré''' 
        for i in range(self.ordre): 
            print(self.tableau[i]) 
                                   
    def somme_ligne(self, i): 
        '''Calcule la somme des valeurs de la ligne i''' 
        somme = 0             
                                   
        for j in range(self.ordre): 
            somme = somme + self.tableau[i][j] 
        return somme          
                                   
    def somme_col(self, j):   
        '''Calcule la somme des valeurs de la colonne j''' 
        somme = 0
                                   
        for i in range(self.ordre): 
            somme = somme + self.tableau[i][j] 
        return somme          
                                   
                                   
    def est_semimagique(self): 
        s = self.somme_ligne(0) 
        #test de la somme de chaque ligne 
        for i in range(...): 
            if ... != s: 
                return ... 
                                   
        #test de la somme de chaque colonne 
        for j in range(...): 
            if ... != s: 
                return ... 
                                   
        return ... 

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
class Carre:
    def __init__(self, liste, n): 
        self.ordre = n        
        self.tableau = [[liste[i + j * n] for i in range(n)] 
                        for j in range(n)] 
                                   
    def affiche(self):        
        '''Affiche un carré''' 
        for i in range(self.ordre): 
            print(self.tableau[i]) 
                                   
    def somme_ligne(self, i): 
        '''Calcule la somme des valeurs de la ligne i''' 
        somme = 0             
                                   
        for j in range(self.ordre): 
            somme = somme + self.tableau[i][j] 
        return somme          
                                   
    def somme_col(self, j):   
        '''Calcule la somme des valeurs de la colonne j''' 
        somme = 0
                                   
        for i in range(self.ordre): 
            somme = somme + self.tableau[i][j] 
        return somme          
                                   
                                   
    def est_semimagique(self): 
        s = self.somme_ligne(0) 
        #test de la somme de chaque ligne 
        for i in range(1, self.ordre): 
            if  self.somme_ligne(i) != s: 
                return False 
                                   
        #test de la somme de chaque colonne 
        for j in range(self.ordre): 
            if self.somme_col(j) != s: 
                return False 
                                   
        return True 


c2 = Carre([1,7,7,1], 2)
c3 = Carre([3, 4, 5, 4, 4, 4, 5, 4, 3], 3)
c3bis = Carre([2,9,4,7,0,3,6,1,8], 3)

assert c2.est_semimagique()
assert c3.est_semimagique()
assert not c3bis.est_semimagique()
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
lst_c3 = [3, 4, 5, 4, 4, 4, 5, 4, 3]
c3 = Carre(lst_c3, 3)
# c3.affiche()
# [3, 4, 5]
# [4, 4, 4]
# [5, 4, 3]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
1 == 1
# --- PYODIDE:post --- #
##########################