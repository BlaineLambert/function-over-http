from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
# Create your views here.

def hello_view(request: HttpRequest, name: HttpRequest) -> HttpRequest:
    return HttpResponse(f"Hey, {name}!")

def how_old(request: HttpRequest, year: HttpRequest, birthyear: HttpRequest) -> HttpRequest:
    return HttpResponse(f"{year - birthyear}")

def order(request: HttpRequest, burber: HttpRequest, fries: HttpRequest, drink: HttpRequest) -> HttpResponse:
    return HttpResponse(f"{burber * 4.5 + drink * 1 + fries * 1.5}")