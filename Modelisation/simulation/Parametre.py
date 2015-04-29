# -*- coding: utf-8 -*-
import ElementEquation

class Parametre(ElementEquation):
     listparametre = []
     def __init__(self,nomParametre,valeur):
        self.nom = nomParametre
        self.valeur= valeur
    
     def Ajouter(self,element):
        self.listparametre.append(element)
    
     def Modifier(self,element):
        NotImplementedError
        
     def Rechercher(self,element):
        NotImplementedError
        
     def Supprimer(self,element):
        self.listparametre.remove(element)

