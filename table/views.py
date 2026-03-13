from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def table(request):
    return HttpResponse("<h1>Bu table sahifasi<h1/>")
def plus1(request):
    return HttpResponse("<h2>Bu plus1<h2/>")