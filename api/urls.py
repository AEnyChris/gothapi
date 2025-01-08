from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('', views.api_root),
    # re_path(r'^stats/?$', views.resources_stats),
    path('stats/', views.resources_stats),
    path('people/', views.PeopleList.as_view(), name='people-list'),
    path('people/<int:pk>/', views.PeopleDetail.as_view(), name='people-detail'),
    path('houses/', views.HouseList.as_view(), name='house-list'),
    path('houses/<int:pk>/', views.HouseDetail.as_view(), name='house-detail'),
    path('places/', views.PlaceList.as_view(), name='place-list'),
    path('places/<int:pk>/', views.PlaceDetail.as_view(), name='place-detail'),
    path('dragons/', views.DragonList.as_view(), name='dragon-list'),
    path('dragons/<int:pk>/', views.DragonDetail.as_view(), name='dragon-detail'),
    path('seasons/', views.SeasonList.as_view(), name='season-list'),
    path('seasons/<int:pk>/', views.SeasonDetail.as_view(), name='season-detail'),
    path('episodes/', views.EpisodeList.as_view(), name='episode-list'),
    path('episodes/<int:pk>/', views.EpisodeDetail.as_view(), name='episode-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)