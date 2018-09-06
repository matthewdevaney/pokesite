from django.db import models


class Pokemon(models.Model):
    """Model representing a pokemon, but not a specific pokemon"""
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    height = models.CharField(max_length=7)
    weight = models.DecimalField(max_digits=5, decimal_places=1)
    category = models.CharField(max_length=20)
    overgrow = models.CharField(max_length=20)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    specattack = models.IntegerField()
    specdefense = models.IntegerField()
    speed = models.IntegerField()
    type1 = models.CharField(max_length=20)
    type2 = models.CharField(max_length=20)
    weakness1 = models.CharField(max_length=20)
    weakness2 = models.CharField(max_length=20)
    weakness3 = models.CharField(max_length=20)
    weakness4 = models.CharField(max_length=20)
    weakness5 = models.CharField(max_length=20)
    weakness6 = models.CharField(max_length=20)
    weakness7 = models.CharField(max_length=20)
    icon = models.ImageField()
    image = models.ImageField()

    def __str__(self):
        return self.name

