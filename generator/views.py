# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    thepassword = ''

    characters = list('abcdefghijklmnopqrstuvwxyz')
    if(request.GET.get('uppercase')):
         characters.extend('ABCDEFHIJKLMNOPQRSTUVWXYZ')

    if(request.GET.get('specialcase')):
        characters.extend('!@#$%^&*()')

    if(request.GET.get('numbers')):
        characters.extend('0123456789')

    length = int(request.GET.get('length'))

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

# Create your views here.
