from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render, get_object_or_404

from coffees.models import Coffee


def index(request):
    coffees = Coffee.objects.all()
    return render(request, 'coffees/index.html', {'coffees': coffees})

def show(request,pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    return render(request, 'coffees/show.html', {"coffee":coffee})