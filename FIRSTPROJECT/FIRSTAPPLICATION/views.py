from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def set(request):
    return HttpResponse("Hello")

def message(request):
    return render(request,"index.html")