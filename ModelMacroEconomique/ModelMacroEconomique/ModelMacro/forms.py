from django import forms
from models import Variable
class VariableForms(forms.ModelForm):
   class Meta:
       models= Variable
    