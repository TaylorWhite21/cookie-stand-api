from django.urls import path
from .views import AnimeList, AnimeDetail

urlpatterns = [
    path("", AnimeList.as_view(), name="anime_list"),
    path("<int:pk>/", AnimeDetail.as_view(), name="anime_detail"),
]
