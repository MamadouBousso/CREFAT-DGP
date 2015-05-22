from django.db import models

# Create your models here.
class Equation(models.Model):
    id_equation = models.IntegerField(db_column='id_Equation', primary_key=True, blank=True, null=False)
    type = models.TextField(blank=True, null=False)

    class Meta:
        db_table = 'Equation'


class EquationHasOperateur(models.Model):
    id_equation = models.ForeignKey(Equation, db_column='id_Equation', blank=True, null=False)
    nom_operateur = models.ForeignKey('Operateur', db_column='nom_Operateur', blank=True, null=False)  

    class Meta:
        db_table = 'Equation_has_Operateur'


class EquationHasParametre(models.Model):
    id_equation = models.ForeignKey(Equation, db_column='id_Equation', blank=True, null=False)  
    nom_parametre = models.TextField(db_column='nom_Parametre', blank=True, null=False) 

    class Meta:
        db_table = 'Equation_has_Parametre'


class EquationHasSequation(models.Model):
    id_equation = models.ForeignKey(Equation, db_column='id_Equation', blank=True, null=False)  
    id_sequation = models.ForeignKey('SEquation', db_column='id_SEquation', blank=True, null=False)  

    class Meta:
        db_table = 'Equation_has_SEquation'


class EquationHasVariable(models.Model):
    id_equation = models.ForeignKey('Equation',db_column='id_Equation', null=False)
    id_Variable = models.ForeignKey('Variable', db_column='id_Variable', null=False)

    class Meta:
        db_table = 'Equation_has_Variable'


class Operateur(models.Model):
    nom_operateur = models.TextField(db_column='nom_Operateur', primary_key=True, blank=True, null=False)

    class Meta:
        db_table = 'Operateur'


class Parametre(models.Model):
    nom_parametre = models.TextField(db_column='nom_Parametre', primary_key=True, blank=True, null=False)
    valeur = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Parametre'


class Profil(models.Model):
    idprofil = models.IntegerField(db_column='idProfil', primary_key=True, blank=True, null=False)  
    nomprofil = models.TextField(db_column='nomProfil', blank=True, null=False)  

    class Meta:
        db_table = 'Profil'


class SEquation(models.Model):
    id_sequation = models.IntegerField(db_column='id_SEquation', primary_key=True, blank=True, null=False)  # Field name made lowercase.

    class Meta:
        db_table = 'S_Equation'


class Secteur(models.Model):
    id_secteur = models.IntegerField(db_column='id_Secteur', primary_key=True, blank=True, null=False) 
    nom_secteur = models.TextField(db_column='nom_Secteur', blank=True, null=False)  

    class Meta:
        db_table = 'Secteur'


class Temps(models.Model):
    annee = models.IntegerField(primary_key=True, blank=True, null=False)

    class Meta:
        db_table = 'Temps'


class Users(models.Model):
    idusers = models.IntegerField(db_column='idUsers', primary_key=True, blank=True, null=False)
    prenom = models.TextField(blank=True, null=True)
    nom = models.TextField(blank=True, null=True)
    login = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)
    idprofil = models.IntegerField(db_column='idProfil', blank=True, null=False)

    class Meta:
        db_table = 'Users'


class Valeur(models.Model):
    id_valeur = models.IntegerField(db_column='id_Valeur', primary_key=True, blank=True, null=False)
    valeur = models.TextField(blank=True, null=True)
    annee = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Valeur'


class Variable(models.Model):
    id_variable = models.IntegerField(db_column='id_Variable', primary_key=True, blank=True, null=False)
    nom_variable = models.TextField(db_column='nom_Variable', blank=True, null=True)  
    typeVariable = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sect_var = models.ForeignKey(Secteur, db_column='id_Secteur', blank=True, null=True)
    id_valeur = models.ForeignKey(Valeur, db_column='id_Valeur', blank=True, null=True)

    class Meta:
        db_table = 'Variable'

