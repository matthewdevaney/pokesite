from django.shortcuts import render
from .models import Pokemon

# Create your views here.


def index(request):
    return render(request, 'pokedex/index.html')


def pokemon_list(request):
    pokemon = Pokemon.objects.order_by('id')
    return render(request, 'pokedex/pokemon_list.html', {'pokemon': pokemon})
