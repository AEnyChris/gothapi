"""
This module defines the models for the GOT API application.

Models:
    Base: abstract base model that includes created_at and updated_at fields.
    People: Represents a person in the GOT universe with various attributes.
    House: Represents a noble house with attributes.
    Place: Represents a location with attributes.
    Dragon: Represents a dragon with attributes.
    Season: Represents a season of the show with various attributes.
    Episode: Represents an episode of the show with various attributes.
"""
from django.db import models


class Base(models.Model):
    """
    Base model: an abstract base class.
    that includes common fields for creation and update timestamps.
    This model will not be used to create any database table.

    Attributes:
        created_at (DateTimeField): The date and time the record was created.
        updated_at (DateTimeField): The date and time the record was last updated.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
       Indicates that this is an abstract base class.
        """
        abstract = True


class People(Base):
    """
    People model representing a character in the API.

    Attributes:
        name (string): The name of the character.
        titles (JSON): A JSON field containing titles of the character
        aliases (object): A JSON field containing aliases of the character.
        gender (string): The gender of the character.
        played_by (string): The actor who played the character.
        birthplace (string): The birthplace of the character.
        houseled (string): url representing house led by the character.
        parents (list): a list of urls representing the parents of the character.
        siblings (list): a list of urls representing the siblings of the character.
        death (string): A description of the character's death.
        episodes (list): a list of urls representing the episodes the character appears in.
    """
    name = models.CharField(max_length=50)
    titles = models.JSONField(null=True)
    aliases = models.JSONField(null=True, blank=True)
    gender = models.CharField(max_length=10, default='', blank=True)
    played_by = models.CharField(max_length=50, default='', blank=True)
    birthplace = models.CharField(max_length=50, default='', blank=True)
    houseled = models.ForeignKey('House', on_delete=models.CASCADE,
                                 null=True, related_name='heads')
    parents = models.ManyToManyField('self', symmetrical=False,
                                     related_name='children')
    siblings = models.ManyToManyField('self', symmetrical=True)
    death = models.CharField(max_length=2048, default='', blank=True)
    episodes = models.ManyToManyField('Episode', related_name='characters')

    def __str__(self):
        return f"{self.id} {self.name}"


class House(Base):
    """
    House model representing a noble house.

    Attributes:
        name (string): The name of the house
        sigil (string): A description of the sigil of the house.
        members (list): A list of url representing members of the house.
        word (string): The words or motto of the house.
        seat (string): url representing the seat of the house.
        places_ruled (list): A list of url representing places ruled by the house
    """
    name = models.CharField(max_length=50)
    sigil = models.CharField(max_length=1024, default='', blank=True)
    members = models.ManyToManyField('People', related_name='allegiances')
    word = models.CharField(max_length=1024)
    seat = models.OneToOneField('Place', on_delete=models.CASCADE, null=True,
                                related_name='seat_of')
    places_ruled = models.ManyToManyField('Place',  related_name='ruled_by')

    def __str__(self):
        return f"{self.id} {self.name}"


class Place(Base):
    """
    Place model representing a location with associated details.

    Attributes:
        name (string): The name of the place.
        description (string): A brief description of the place.
        region (string): The region where the place is located
        events (string): Events associated with the place.
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=2048, default='', blank=True)
    region = models.CharField(max_length=50, default='', blank=True)
    events = models.CharField(max_length=2048, default='', blank=True)

    def __str__(self):
        return f"{self.id} {self.name}"


class Dragon(Base):
    """
    Dragon model representing a dragon in the system.

    Attributes:
        name (string): The name of the dragon.
        original_rider (string): A url representing the original rider of the dragon.
        riders (array): a list of urls representing all riders of the dragon.
        color (string): The color of the dragon.
        size (string): The size of the dragon.
        facts (string): Additional facts about the dragon.
        death (string): Information about the death of the dragon.
        episodes (array): a list of urls representing the episodes in which the dragon appears.
    """
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
    """
    Represents a season of the Game of Thrones TV show.

    Attributes:
        number (int): The season number.
        number_of_episodes (int): The number of episodes in the season.
        premiere_date (date): The premiere date of the season.
        show_period (string): The period during which the show aired.
        rating (float): The rating of the season.
        budget (float): The budget of the season.
    """
    number = models.IntegerField()
    number_of_episodes = models.IntegerField()
    premiere_date = models.DateField(null=True)
    show_period = models.CharField(max_length=50, default='', blank=True)
    rating = models.FloatField(null=True)
    budget = models.FloatField(null=True)

    def __str__(self):
        return f"Season {self.number}"


class Episode(Base):
    """
    Represents an episode of the Game of Thrones TV show.
    Attributes:
        title (string): The title of the episode.
        num_in_season (int): The episode number within the season.
        num_overall (int): The overall episode number across all seasons.
        director (string): The director of the episode.
        written_by (string): The writer of the episode.
        original_air_date (date): The original air date of the episode.
        synopsis (string): A brief summary of the episode.
        runtime (int): The runtime of the episode in minutes.
        rating (float): The rating of the episode.
        budget (float): The budget of the episode.
        season (Season): The season to which the episode belongs.
    """
    title = models.CharField(max_length=1024)
    num_in_season = models.IntegerField(null=True)
    num_overall = models.IntegerField(null=True)
    director = models.CharField(max_length=50, default='', blank=True)
    written_by = models.CharField(max_length=50, default='', blank=True)
    original_air_date = models.DateField()
    synopsis = models.CharField(max_length=2048, default='',
                                blank=True)
    runtime = models.IntegerField()
    rating = models.FloatField(null=True)
    budget = models.FloatField(null=True)
    season = models.ForeignKey('Season', on_delete=models.CASCADE,
                               null=True, related_name='episodes')

    def __str__(self):
        return f"{self.season} Episode {self.num_in_season}: {self.title}"
