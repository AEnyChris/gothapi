from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from api.models import *
from api.serializers import *
from rest_framework import generics


# Create your views here.
@api_view(['GET'])
def api_root(request, fmt=None):
    """
    Root of the API, providing links to all resources.
    """
    return Response({
        'people': reverse('people-list', request=request, format=fmt),
        'houses': reverse('house-list', request=request, format=fmt),
        'places': reverse('place-list', request=request, format=fmt),
        'dragons': reverse('dragon-list', request=request, format=fmt),
        'seasons': reverse('season-list', request=request, format=fmt),
        'episodes': reverse('episode-list', request=request, format=fmt)
    })

@api_view(['GET'])
def resources_stats(request, format=None):
    """
    Retrieve the count of various resources in the database.

    Args:
        request (HttpRequest): The HTTP request object.
        format (str, optional): The format of the response. Defaults to None.

    Returns:
        Response: A JSON response containing the count of People, House, Place, Dragon, Season, and Episode objects.
    """
    return Response({
        'People': People.objects.count(),
        'House': House.objects.count(),
        'Place': Place.objects.count(),
        'Dragon': Dragon.objects.count(),
        'Season': Season.objects.count(),
        'Episode': Episode.objects.count()
    })

class PeopleList(generics.ListAPIView):
    """
    API view to retrieve list of people.
    """
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

class PeopleDetail(generics.RetrieveAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

class HouseList(generics.ListAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class HouseDetail(generics.RetrieveAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class PlaceList(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceDetail(generics.RetrieveAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class DragonList(generics.ListAPIView):
    queryset = Dragon.objects.all()
    serializer_class = DragonSerializer

class DragonDetail(generics.RetrieveAPIView):
    queryset = Dragon.objects.all()
    serializer_class = DragonSerializer

class SeasonList(generics.ListAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

class SeasonDetail(generics.RetrieveAPIView):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

class EpisodeList(generics.ListAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

class EpisodeDetail(generics.RetrieveAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer