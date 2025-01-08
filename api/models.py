"""
This module defines the models for the GOT API application.

Models:
    Base: An abstract base model that includes created_at and updated_at fields.
    People: Represents a person in the GOT universe with various attributes and relationships.
    House: Represents a noble house with attributes and relationships to people and places.
    Place: Represents a location with attributes and relationships to houses.
    Dragon: Represents a dragon with attributes and relationships to people, seasons, and episodes.
    Season: Represents a season of the show with various attributes.
    Episode: Represents an episode of the show with various attributes and a relationship to a season.
"""
from django.db import models

# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True

class People(Base):
    name = models.CharField(max_length=50)
    titles = models.JSONField(null=True)
    aliases = models.JSONField(null=True, blank=True)
    gender = models.CharField(max_length=10, default='', blank=True)
    played_by = models.CharField(max_length=50, default='', blank=True)
    birthplace = models.CharField(max_length=50, default='', blank=True)
    houseled = models.ForeignKey('House', on_delete=models.CASCADE, null=True, related_name='heads')
    parents = models.ManyToManyField('self', symmetrical=False, related_name='children')
    siblings = models.ManyToManyField('self', symmetrical=True)
    death = models.CharField(max_length=2048, default='', blank=True)
    episodes = models.ManyToManyField('Episode', related_name='characters')

    def __str__(self):
        return f"{self.id} {self.name}"


class House(Base):
    name = models.CharField(max_length=50)
    sigil = models.CharField(max_length=1024, default='', blank=True)
    members = models.ManyToManyField('People', related_name='allegiances')
    word = models.CharField(max_length=1024)
    seat = models.OneToOneField('Place', on_delete=models.CASCADE, null=True, related_name='seat_of')
    places_ruled = models.ForeignKey('Place', on_delete=models.CASCADE, null=True, related_name='ruled_by')

    def __str__(self):
        return f"{self.id} {self.name}"

class Place(Base):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=2048, default='', blank=True)
    region = models.CharField(max_length=50, default='', blank=True)
    events = models.CharField(max_length=2048, default='', blank=True)

    def __str__(self):
        return f"{self.id} {self.name}"


class Dragon(Base):
    name = models.CharField(max_length=50)
    original_rider = models.ForeignKey('People', on_delete=models.CASCADE,
                                       related_name='dragons_owned',
                                       null=True)
    riders = models.ManyToManyField('People', related_name='dragons_ridden')
    color = models.CharField(max_length=50, default='', blank=True)
    size = models.CharField(max_length=1024, default='', blank=True)
    facts = models.CharField(max_length=2048, default='', blank=True)
    death = models.CharField(max_length=2048, default='', blank=True)
    episodes = models.ManyToManyField('Episode', related_name='dragons')

    def __str__(self):
        return f"{self.id} {self.name}"

class Season(Base):
    number = models.IntegerField()
    number_of_episodes = models.IntegerField()
    premiere_date = models.DateField(null=True)
    show_period = models.CharField(max_length=50, default='', blank=True)
    rating = models.FloatField(null=True)
    budget = models.FloatField(null=True)

    def __str__(self):
        return f"Season {self.number}"

class Episode(Base):
    title = models.CharField(max_length=1024)
    num_in_season = models.IntegerField(null=True)
    num_overall = models.IntegerField(null=True)
    director = models.CharField(max_length=50, default='', blank=True)
    written_by = models.CharField(max_length=50, default='', blank=True)
    original_air_date = models.DateField()
    synopsis = models.CharField(max_length=2048, default='', blank=True)
    runtime = models.IntegerField()
    rating = models.FloatField(null=True)
    budget = models.FloatField(null=True)
    season = models.ForeignKey('Season', on_delete=models.CASCADE, null=True, related_name='episodes')

    def __str__(self):
        return f"{self.season} Episode {self.num_in_season}: {self.title}"