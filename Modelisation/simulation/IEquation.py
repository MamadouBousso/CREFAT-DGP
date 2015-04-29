# -*- coding: utf-8 -*-

class IEquation:
    listElement={}
    
    def AjouterElementEquation(self,cle,valeur):
       raise NotImplementedError
    
    def ModifierElementEquation(self,cle,valeur):
        raise NotImplementedError
       
    def RechercherPositionElement(self,valeur):
        raise NotImplementedError
    
    def SupprimerElementEquation(self,valeur):
        raise NotImplementedError