from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Welcome to the Parts & Document Number Registry")


def part_view(request):
    return HttpResponse("Part")
