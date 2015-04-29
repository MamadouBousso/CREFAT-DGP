# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 12:22:04 2015

@author: Karim Ba 
"""
import sqlite3
rep = "/Users/mac/CREFAT-DGP2/CREFAT-DGP/bd_modeleMacro.sq3"

db_loc = sqlite3.connect(rep)
cursor = db_loc.cursor()
cursor.execute('''CREATE TABLE Secteur(id_Secteur Integer PRIMARY KEY, nom_Secteur Text);''')
cursor.execute('''CREATE TABLE Variable(nom_Variable Text PRIMARY KEY,
type TEXT, description TEXT, sect_var INTEGER, FOREIGN KEY(sect_var) REFERENCES Secteur(id_Secteur));''')
cursor.execute('''CREATE TABLE Operateur(nom_Operateur Text PRIMARY KEY);''')
cursor.execute('''CREATE TABLE Constante(nom_Constante Text PRIMARY KEY,
valeur FLOAT);''')
cursor.execute('''CREATE TABLE Equation(id_Equation Integer PRIMARY KEY,
type TEXT);''')
cursor.execute('''CREATE TABLE S_Equation(id_SEquation Integer PRIMARY KEY);''')

cursor.execute('''CREATE TABLE Equation_has_SEquation(id_Equation Integer,id_SEquation Integer,
FOREIGN KEY(id_Equation) REFERENCES Equation(id_Equation),
FOREIGN KEY(id_SEquation) REFERENCES S_Equation(id_SEquation));''')

cursor.execute('''CREATE TABLE Equation_has_Variable(id_Equ Integer ,nom_Var Text,PRIMARY KEY(id_Equ,nom_Var)
FOREIGN KEY(id_Equ) REFERENCES Equation(id_Equation),
FOREIGN KEY(nom_Var) REFERENCES Variable(nom_Variable));''')

cursor.execute('''CREATE TABLE Equation_has_Operateur(id_Equation Integer,nom_Operateur Text,
FOREIGN KEY(id_Equation) REFERENCES Equation(id_Equation),
FOREIGN KEY(nom_Operateur) REFERENCES Operateur(nom_Operateur));''')

cursor.execute('''CREATE TABLE Equation_has_Constante(id_Equation Integer,nom_Constante Text,
FOREIGN KEY(id_Equation) REFERENCES Equation(id_Equation),
FOREIGN KEY(nom_Constante) REFERENCES Constante(nom_Constante));''')
db_loc.commit();
