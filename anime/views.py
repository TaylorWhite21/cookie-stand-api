from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Anime
from .permissions import IsOwnerOrReadOnly
from .serializers import AnimeSerializer


class AnimeList(ListCreateAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer


class AnimeDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializer
