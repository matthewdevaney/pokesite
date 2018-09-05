from django.db import models


class Pokemon(models.Model):
    """Model representing a pokemon, but not a specific pokemon"""
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=300)
    height = models.TextField(max_length=7)
    weight = models.DecimalField(max_digits=5, decimal_places=1)
    category = models.TextField(max_length=20)
    overgrow = models.TextField(max_length=20)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    specattack = models.IntegerField()
    specdefense = models.IntegerField()
    speed = models.IntegerField()
    type1 = models.TextField(max_length=20)
    type2 = models.TextField(max_length=20)
    weakness1 = models.TextField(max_length=20)
    weakness2 = models.TextField(max_length=20)
    weakness3 = models.TextField(max_length=20)
    weakness4 = models.TextField(max_length=20)
    weakness5 = models.TextField(max_length=20)
    weakness6 = models.TextField(max_length=20)
    weakness7 = models.TextField(max_length=20)

    def __str__(self):
        return self.name

