
from django.shortcuts import render
from django.views.generic import ListView
from .models import *

# Create your views here.cla
class Infolist(ListView):
    model=Info
    template_name = 'home.html'
