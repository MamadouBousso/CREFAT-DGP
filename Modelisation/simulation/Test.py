# -*- coding: utf-8 -*-
import SystemeEquation
import Equation
import Parametre
import Operateur
import Variable
class Test:
    
    def main(self):
        systeme = SystemeEquation(idSysteme=1)
        equation1 = Equation(1,"second degres","Comptable","Il permet de compter")
        equation2 = Equation(2,"second degres","Comptable","Il permet de compter")
        v1 = Variable(nomVariable="X")
        v2 = Variable(nomVariable="Y")
        v3 = Variable(nomVariable="Z")
        op1 = Operateur(nomOperateur="+")
        op2 = Operateur(nomOperateur="-")
        op3= Operateur(nomOperateur="=")
        param = Parametre(nomParametre="2")
        equation1.AjouterElementEquation(1,v1)
        equation1.AjouterElementEquation(2,op1)
        equation1.AjouterElementEquation(3,v2)
        equation1.AjouterElementEquation(4,op2)
        equation1.AjouterElementEquation(5,v3)
        equation1.AjouterElementEquation(6,op3)
        equation1.AjouterElementEquation(6,param)
        systeme.AjouterElementEquation(equation1)
        systeme.AjouterElementEquation(equation2)
        systeme.afficherSysteeme()