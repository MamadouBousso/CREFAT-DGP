# -*- coding: utf-8 -*-
import ElementEquation
class Operateur(ElementEquation):
     listOperateur = []
     def __init__(self,nomOperateur):
        self.nom = nomOperateur
    
     def Ajouter(self,element):
        self.listOperateur.append(element)
    
     def Modifier(self,element):
        NotImplementedError
        
     def Rechercher(self,element):
        NotImplementedError
        
     def Supprimer(self,element):
        self.listOperateur.remove(element)