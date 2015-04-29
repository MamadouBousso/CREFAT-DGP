# -*- coding: utf-8 -*-
import IEquation
class Equation(IEquation):
    
    listElement={}
    def __init__(self,idEquation,nomEquation,natureEquation,details):
        self.idEquation = idEquation
        self.nomEquation = nomEquation
        self.natureEquation = natureEquation
        self.details = details
    
    def AjouterElementEquation(self,cle,valeur):
        self.listElement[cle]=valeur
    
    def ModifierElementEquation(self,cle,valeur):
        if(self.listElement[cle]==None):
            print("La clé n'existe pas")
        else:
            self.listElement[cle]=valeur
            
    def RechercherPositionElement(self,valeur):
        for valeur in self.listElement:
            return self.listElement[valeur]
    def aficheEquation(self):
        for element in self.listElement:
            print(element)
         
        
        