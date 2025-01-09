"""
AUTHOR: Enyone Christian Achobe

This module contains serializers for the models in the API.

Serializers:
    - HouseSerializer: Serializer for the House model.
    - PeopleSerializer: Serializer for the People model.
    - PlaceSerializer: Serializer for the Place model.
    - DragonSerializer: Serializer for the Dragon model.
    - SeasonSerializer: Serializer for the Season model.
    - EpisodeSerializer: Serializer for the Episode model.

Each serializer converts model instances to JSON format
and includes related fields as hyperlinks.
"""
from rest_framework import serializers
from api.models import House, Place, People, Dragon, Season, Episode


class HouseSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the House model.
    """
    head = serializers.HyperlinkedRelatedField(
        many=True, view_name='people-detail', read_only=True)

    class Meta:
        model = House
        fields = '__all__'


class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the People model.
    """
    allegiances = serializers.HyperlinkedRelatedField(
        many=True, view_name='house-detail', read_only=True)
    dragons_owned = serializers.HyperlinkedRelatedField(
        many=True, view_name='dragon-detail', read_only=True)
    dragons_ridden = serializers.HyperlinkedRelatedField(
        many=True, view_name='dragon-detail', read_only=True)

    class Meta:
        model = People
        fields = '__all__'


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Place model.
    """
    seat_of = serializers.HyperlinkedRelatedField(
        many=True, view_name='house-detail', read_only=True)
    ruled_by = serializers.HyperlinkedRelatedField(
        many=True, view_name='house-detail', read_only=True)

    class Meta:
        model = Place
        fields = '__all__'


class DragonSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Dragon model.
    """
    class Meta:
        model = Dragon
        fields = '__all__'


class SeasonSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Season model.
    """
    episodes = serializers.HyperlinkedRelatedField(
        many=True, view_name='episode-detail', read_only=True)

    class Meta:
        model = Season
        fields = '__all__'


class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Episode model.
    """
    characters = serializers.HyperlinkedRelatedField(
        many=True, view_name='people-detail', read_only=True)
    dragons = serializers.HyperlinkedRelatedField(
        many=True, view_name='dragon-detail', read_only=True)

    class Meta:
        model = Episode
        fields = '__all__'