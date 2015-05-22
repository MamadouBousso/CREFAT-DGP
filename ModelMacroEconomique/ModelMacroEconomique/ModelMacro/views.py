#from django.shortcuts import render
#-*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, loader
from datetime import datetime
from django.shortcuts import render
from .models import Variable

# Create your views here.
def index(request):
    template = loader.get_template('ModelMacro/index.html')
    context = RequestContext(request, None)
    return HttpResponse(template.render(context))
def variable(request):
    variable = Variable.objects.all()
    return render(request, 'ModelMacro/Variable.html', {'variables': variable})
def equation(request):
    template = loader.get_template('ModelMacro/equation.html')
    context = RequestContext(request, None)
    return HttpResponse(template.render(context))
def parametrage(request):
    template = loader.get_template('ModelMacro/parametrage.html')
    context = RequestContext(request, None)
    return HttpResponse(template.render(context))
def systeme(request):
    template = loader.get_template('ModelMacro/systeme.html')
    context = RequestContext(request, None)
    return HttpResponse(template.render(context))
def date_actuelle(request):
    return render(request, 'ModelMacro/date.html', {'date': datetime.now()})
