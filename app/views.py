from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
# Create your views here.

def hello_view(request, name):
    return HttpResponse(f"Hey, {name}!")

def how_old(request, year, birthyear):
    return HttpResponse(f"{year - birthyear}")

def order(request, burber, fries, drink):
    return HttpResponse(f"{burber * 4.5 + drink * 1 + fries * 1.5}")