from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


rooms = [
    {'id':1, 'name':'Lets learn something'},
    {'id':2, 'name':'Lets learn python'},
    {'id':3, 'name':'Lets learn django'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)

def room (request):
    return render(request, 'room.html')
