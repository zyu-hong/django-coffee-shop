from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render

from coffees.models import Coffee


def index(request):
    coffees = Coffee.objects.all()
    return render(request, 'coffees/index.html', {'coffees': coffees})

