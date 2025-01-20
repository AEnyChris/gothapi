from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from api import views

# Create a router and register our ViewSets with it.
router = DefaultRouter(trailing_slash=True)
router.register(r'api/people', views.PeopleViewSet, basename='people')
router.register(r'api/places', views.PlaceViewSet, basename='place')
router.register(r'api/houses', views.HouseViewSet, basename='house')
router.register(r'api/dragons', views.DragonViewSet, basename='dragon')
router.register(r'api/seasons', views.SeasonViewSet, basename='season')
router.register(r'api/episodes', views.EpisodeViewSet, basename='episode')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    re_path('^stats/?$', views.resources_stats),
    re_path('^home/?$', views.HomePage.as_view())
]