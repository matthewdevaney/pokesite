from django import forms
from .models import Pokemon


class PokemonForm(forms.ModelForm):

    class Meta:
        model = Pokemon
        fields = ['id', 'name', 'description', 'icon']

    """
    id = forms.IntegerField(label='Pokemon ID#')
    name = forms.CharField(label='Pokemon')
    description = forms.CharField(label='Description')
    height = forms.CharField(label='Height (ft)')
    weight = forms.DecimalField(label='Weight (lbs')
    category = forms.CharField(label='Category')
    overgrow = forms.CharField(label='overgrow')
    hp = forms.IntegerField(label='HP')
    attack = forms.IntegerField(label='Attack')
    defense = forms.IntegerField(label='Defense')
    specattack = forms.IntegerField(label='Special Attack')
    specdefense = forms.IntegerField(label='Special Defense')
    speed = forms.IntegerField(label='Speed')
    type1 = forms.CharField(label='Type 1')
    type2 = forms.CharField(label='Type 2')
    weakness1 = forms.CharField(label='Weakness 1')
    weakness2 = forms.CharField(label='Weakness 2')
    weakness3 = forms.CharField(label='Weakness 3')
    weakness4 = forms.CharField(label='Weakness 4')
    weakness5 = forms.CharField(label='Weakness 5')
    weakness6 = forms.CharField(label='Weakness 6')
    weakness7 = forms.CharField(label='Weakness 7')
    image = forms.ImageField(label='image')
    icon = forms.ImageField(label='Icon')
     """

