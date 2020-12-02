from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def temp(request):
    return HttpResponse('Hello! Your app is working properly.')