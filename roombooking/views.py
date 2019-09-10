from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404
#from django.http import HttpResponse
#from .models import Room

# Create your views here.

class HomeView(TemplateView):
    template_name = 'roombooking/index.html'
    