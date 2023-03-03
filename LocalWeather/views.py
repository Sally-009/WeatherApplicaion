from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import currentConditions

# Create your views here.
def index(request):
    dataPage = currentConditions.returnData # the whole data
    prop = currentConditions.properties     # properties
    periods = currentConditions.periods     # periods
    
    template = loader.get_template('home.html') # HTTP template
    context = {
        'dataPage': dataPage,
        'properties' : prop,
        'periods' : periods,
    }
    return HttpResponse(template.render(context, request))