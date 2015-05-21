import Equation 
class SystemeEquation(Equation):
    listEquation = []
    def __init__(self,idSysteme):
        self.idSysteme = idSysteme
    
    def AjouterElementEquation(self,cle,valeur):
        self.listEquation[cle]=valeur
    
    def ModifierElementEquation(self,cle,valeur):
        if(self.listEquation[cle]==None):
            print("La clé n'existe pas")
        else:
            self.listEquation[cle]=valeur
            
    def RechercherPositionElement(self,valeur):
        for valeur in self.listEquation:
            return self.listEquation[valeur]
    def afficherSysteeme(self):
        for equation in self.listEquation:
            print(equation)
        