from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from api.models import *
from api.serializers import *
from django.shortcuts import render

# Create your views here.
@api_view(['GET'])
def resources_stats(request, format=None):
    """
    Retrieve the count of various resources in the database.
    Returns:
        Response: A JSON response containing the count of each resource
    """
    return Response({
        'People': People.objects.count(),
        'House': House.objects.count(),
        'Place': Place.objects.count(),
        'Dragon': Dragon.objects.count(),
        'Season': Season.objects.count(),
        'Episode': Episode.objects.count()
    })


# def homepage(request):
#     return render(request, 'rest_framework/home.html')

class HomePage(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'rest_framework/home.html'

    def get(self, request):
        queryset = People.objects.all()
        return Response({'people': queryset})

class PeopleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Provides `list` and `retrieve` actions for  the People resource.
    """
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    


class HouseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class PlaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class DragonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dragon.objects.all()
    serializer_class = DragonSerializer

class SeasonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

class EpisodeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
