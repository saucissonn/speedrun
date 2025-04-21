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

def nombre_lignes(image):
    '''renvoie le nombre de lignes de l'image'''
    return ... 

def nombre_colonnes(image):
    '''renvoie la largeur de l'image'''
    return ... 

def negatif(image):
    '''renvoie le negatif de l'image sous la forme
       d'une liste de listes'''
    # on cree une image de 0 aux memes dimensions 
    # que le parametre image
    nouvelle_image = [[0 for k in range(nombre_colonnes(image))]
         for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(...): 
            nouvelle_image[i][j] = ... 
    return nouvelle_image

def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inferieure au seuil et 255 sinon'''
    nouvelle_image = [[0] * nombre_colonnes(image)
                      for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(...): 
            if image[i][j] < ... : 
                nouvelle_image[i][j] = ... 
            else:
                nouvelle_image[i][j] = ... 
    return nouvelle_image

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
def nombre_lignes(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image) 

def nombre_colonnes(image):
    '''renvoie la largeur de l'image'''
    return len(image[0]) 

def negatif(image):
    '''renvoie le negatif de l'image sous la forme
       d'une liste de listes'''
    # on cree une image de 0 aux memes dimensions 
    # que le parametre image
    nouvelle_image = [[0 for k in range(nombre_colonnes(image))]
         for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(nombre_colonnes(image)): 
            nouvelle_image[i][j] = 255 - image[i][j] 
    return nouvelle_image

def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inferieure au seuil et 1 sinon'''
    nouvelle_image = [[0 for k in range(nombre_colonnes(image))] 
         for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(nombre_colonnes(image)): 
            if image[i][j] < seuil : 
                nouvelle_image[i][j] = 0 
            else:
                nouvelle_image[i][j] = 1 
    return nouvelle_image
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
img = [[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]
assert nombre_lignes(img) == 4
assert nombre_colonnes(img) == 5
assert negatif(img) == [[235, 221, 1, 110, 249], [232, 131, 18, 30, 186], [58, 81, 48, 230, 168], [0, 255, 231, 58, 66]]
assert binaire(img,120) == [[0, 0, 255, 255, 0],[0, 255, 255, 255, 0], [255, 255, 255, 0, 0],[255, 0, 0, 255, 255]]
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
img = [[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]
assert nombre_lignes(img) == 4
assert nombre_colonnes(img) == 5
assert negatif(img) == [[235, 221, 1, 110, 249], [232, 131, 18, 30, 186], [58, 81, 48, 230, 168], [0, 255, 231, 58, 66]]
assert binaire(img,120) == [[0, 0, 255, 255, 0],[0, 255, 255, 255, 0], [255, 255, 255, 0, 0],[255, 0, 0, 255, 255]]
# --- PYODIDE:post --- #
##########################