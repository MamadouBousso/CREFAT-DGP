from django.contrib import admin
from .models import Equation, Variable,Operateur, Valeur,Temps, Users, SEquation,Secteur,Parametre, Profil

# Register your models here.
admin.site.register(Equation)
admin.site.register(Variable)
admin.site.register(Operateur)
admin.site.register(Valeur)
admin.site.register(Temps)
admin.site.register(Users)
admin.site.register(SEquation)
admin.site.register(Secteur)
admin.site.register(Parametre)
admin.site.register(Profil)