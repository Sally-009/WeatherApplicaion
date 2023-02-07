from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import currentConditions

# Create your views here.
def index(request):
    dataPage = currentConditions.returnData
    template = loader.get_template('home.html')
    context = {
        'dataPage': dataPage,
    }
    return HttpResponse(template.render(context, request))