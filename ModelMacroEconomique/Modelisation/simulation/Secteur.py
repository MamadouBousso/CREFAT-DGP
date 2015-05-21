# -*- coding: utf-8 -*-
import ElementEquation
class Secteur(ElementEquation):
     listSecteur = []
     def __init__(self,nomOperateur):
        self.nom = nomOperateur
    
     def Ajouter(self,element):
        self.listSecteur.append(element)
    
     def Modifier(self,element):
        NotImplementedError
        
     def Rechercher(self,element):
        NotImplementedError
        
     def Supprimer(self,element):
        self.listSecteur.remove(element)

