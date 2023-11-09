from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
# Create your views here.

def hello_view(request: HttpRequest, name: str) -> HttpResponse:
    return HttpResponse(f"Hey, {name}!")

def how_old(request: HttpRequest, year: int, birthyear: int) -> HttpResponse:
    return HttpResponse(f"{year - birthyear}")

def order(request: HttpRequest, burber: int, fries: int, drink: int) -> HttpResponse:
    return HttpResponse(f"{burber * 4.5 + drink * 1 + fries * 1.5}")