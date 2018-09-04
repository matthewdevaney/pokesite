from django.db import models


class ElementType(models.Model):
    """Model representing pokemon elemental types"""
    element = models.TextField(max_length=20)

    def __str__(self):
        return self.element


class Pokemon(models.Model):
    """Model representing a pokemon, but not a specific pokemon"""
    id = models.IntegerField()
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=300)
    height = models.TextField(max_length=7)
    weight = models.DecimalField(max_digits=4, decimal_places=1)
    category = models.TextField(max_length=20)
    overgrow = models.TextField(max_length=20)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    specattack = models.IntegerField()
    specdefense = models.IntegerField()
    speed = models.IntegerField()
    type = models.ManyToManyField(ElementType)
    weakness = models.ManyToManyField(ElementType)

    def __str__(self):
        return self.name

