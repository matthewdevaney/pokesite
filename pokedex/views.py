from django.shortcuts import render, redirect
from .models import Pokemon
from .forms import PokemonForm

# Create your views here.


def index(request):
    return render(request, 'pokedex/index.html')


def pokemon_list(request):
    pokemon = Pokemon.objects.order_by('id')
    return render(request, 'pokedex/pokemon_list.html', {'pokemon': pokemon})


def pokemon_add(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            return redirect(request, 'pokedex/pokemon_list.html')
    else:
        form = PokemonForm()
    return render(request, 'pokedex/pokemon_add.html', {'form': form})
