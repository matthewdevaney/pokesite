from django.shortcuts import render, redirect
from .models import Pokemon
from .forms import PokemonForm

# Create your views here.


def index(request):
    return render(request, 'pokedex/index.html')


def pokemon_list(request):
    pokemon = Pokemon.objects.order_by('id')
    return render(request, 'pokemon_list.html', {'pokemon': pokemon})


def pokemon_add(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pokemon_list')
        else:
            print(form.errors)
    else:
        form = PokemonForm()
    return render(request, 'pokemon_add.html', {'form': form})
