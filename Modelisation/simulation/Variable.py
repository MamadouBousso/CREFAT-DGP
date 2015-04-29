# -*- coding: utf-8 -*-
import ElementEquation
class Variable(ElementEquation):
    
    listVariable = []
    def __init__(self,idVariable,nomVariable,natureVariable,details):
        self.idVariable = idVariable
        self.nomVariable= nomVariable
        self.natureVariable= natureVariable
        self.details= details
    
    def Ajouter(self,element):
        self.listVariable.append(element)
    
    def Modifier(self,element):
        NotImplementedError
        
    def Rechercher(self,element):
        NotImplementedError
        
    def Supprimer(self,element):
        self.listVariable.remove(element)
