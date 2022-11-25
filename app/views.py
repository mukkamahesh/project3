from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('mahesh loves alcohol')
def propose(request):
    return HttpResponse('<marquee>yes i love u too</marquee>')
def mahesh(request):
    return HttpResponse('<h1>handsome guy</h1>')
