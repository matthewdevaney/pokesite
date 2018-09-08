from django.db import models


class Pokemon(models.Model):
    """Model representing a pokemon, but not a specific pokemon"""
    id = models.IntegerField(primary_key=True, help_text='Pokemon ID')
    name = models.CharField(max_length=50, help_text='Pokemon')
    description = models.CharField(max_length=300, help_text='Description')
    height = models.CharField(max_length=7)
    weight = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    category = models.CharField(max_length=20)
    overgrow = models.CharField(max_length=20)
    hp = models.IntegerField(blank=True, null=True)
    attack = models.IntegerField(blank=True, null=True)
    defense = models.IntegerField(blank=True, null=True)
    specattack = models.IntegerField(blank=True, null=True)
    specdefense = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    type1 = models.CharField(max_length=20)
    type2 = models.CharField(max_length=20)
    weakness1 = models.CharField(max_length=20)
    weakness2 = models.CharField(max_length=20)
    weakness3 = models.CharField(max_length=20)
    weakness4 = models.CharField(max_length=20)
    weakness5 = models.CharField(max_length=20)
    weakness6 = models.CharField(max_length=20)
    weakness7 = models.CharField(max_length=20)
    image = models.ImageField(upload_to='')
    icon = models.ImageField(upload_to='')

    def __str__(self):
        return self.name

