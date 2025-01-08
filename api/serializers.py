from rest_framework import serializers
from api.models import House, Place, People, Dragon, Season, Episode



class HouseSerializer(serializers.HyperlinkedModelSerializer):
    head = serializers.HyperlinkedRelatedField(many=True, view_name='people-detail', read_only=True)

    class Meta:
        model = House
        fields = '__all__'


class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    allegiances = serializers.HyperlinkedRelatedField(many=True, view_name='house-detail', read_only=True)
    dragons_owned = serializers.HyperlinkedRelatedField(many=True, view_name='dragon-detail', read_only=True)
    dragons_ridden = serializers.HyperlinkedRelatedField(many=True, view_name='dragon-detail', read_only=True)

    class Meta:
        model = People
        fields = '__all__'


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    seat_of = serializers.HyperlinkedRelatedField(many=True, view_name='house-detail', read_only=True)
    ruled_by = serializers.HyperlinkedRelatedField(many=True, view_name='house-detail', read_only=True)

    class Meta:
        model = Place
        fields = '__all__'


class DragonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dragon
        fields = '__all__'


class SeasonSerializer(serializers.HyperlinkedModelSerializer):
    episodes = serializers.HyperlinkedRelatedField(many=True, view_name='episode-detail', read_only=True)

    class Meta:
        model = Season
        fields = '__all__'

class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    characters = serializers.HyperlinkedRelatedField(many=True, view_name='people-detail', read_only=True)
    dragons = serializers.HyperlinkedRelatedField(many=True, view_name='dragon-detail', read_only=True)

    class Meta:
        model = Episode
        fields = '__all__'