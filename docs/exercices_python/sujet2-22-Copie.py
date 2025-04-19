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

class AdresseIP:
    def __init__(self, adresse):
        self.adresse =... 

    def liste_octets(self):
        """renvoie une liste de nombres entiers,
        la liste des octets de l'adresse IP"""
        # Note : split découpe la chaine de caractères 
        # en fonction du séparateur
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
        réservée, False sinon"""
        reservees = [ ... ] 
        return ... 

    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse
        IP qui suit l'adresse self si elle existe et None sinon"""
        octets = ... 
        if ... == 254: 
            return None
        octet_nouveau = ... + ... 
        return AdresseIP('192.168.0.' + ...) 

# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:corr --- #
class AdresseIP:
    def __init__(self, adresse):
        self.adresse = adresse

    def liste_octets(self):
        """renvoie une liste de nombres entiers,
        la liste des octets de l'adresse IP"""
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
        réservée, False sinon"""
        reservees = [ '192.168.0.0', '192,168.0,255' ] 
        return self.adresse in reservees 

    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse
        IP qui suit l'adresse self si elle existe et None sinon"""
        octets = self.liste_octets() 
        if octets[3] == 254: 
            return None
        octet_nouveau = octets[3] + 1 
        return AdresseIP('192.168.0.' + str(octet_nouveau)) 

adresse1 = AdresseIP('192.168.0.1')
adresse2 = AdresseIP('192.168.0.2')
adresse3 = AdresseIP('192.168.0.0')
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:tests --- #
assert adresse1.liste_octets() == [192, 168, 0, 1]
assert not adresse1.est_reservee()
assert adresse3.est_reservee()
assert adresse2.adresse_suivante().adresse == '192.168.0.3'
# --- PYODIDE:ignore --- #
##########################
# --- PYODIDE:secrets --- #
assert adresse1.liste_octets() == [192, 168, 0, 1]
assert not adresse1.est_reservee()
assert adresse3.est_reservee()
assert adresse2.adresse_suivante().adresse == '192.168.0.3'
# --- PYODIDE:post --- #
##########################