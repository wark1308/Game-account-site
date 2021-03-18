from django.shortcuts import render
from rest_framework import generics, status, viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from .pagination import ListPagination
from .models import *
from .serializers import *



class GameListView(generics.ListAPIView):
    serializer_class = GameSerializer
    pagination_class = ListPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('title', 'info', 'author__email')
    search_fields = ('title', 'info', 'author__email')
    permission_classes = [permissions.IsAuthenticated]

# class GameUpdate(generics.UpdateAPIView):
    

class GameDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = GameDetailSerializer
    


class GameCreate(generics.CreateAPIView):
    serializer_class = GameCreateSerializer

    def get_serializer_context(self):
        context = super(GameCreate, self).get_serializer_context()
        context.update({
        'owner': self.request.user
        })
        return context


# class GameDelete(generics.DestroyAPIView)