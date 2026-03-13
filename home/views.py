from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # return HttpResponse("Bu index sahifasi")
    return HttpResponse("<h1>Bu index sahifasi<h1/>")

def home(request):
    return HttpResponse("Bu home sahifasi")