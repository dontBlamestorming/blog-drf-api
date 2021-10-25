from .models import Category, Post

from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import PostSerializer, CategorySerializer


class PostViewSet(viewsets.ViewSet):
    """ Whole post listing or retrieving by id """

    # def list(self, request):
    #     queryset = Post.objects.all()
    #     serializer = PostListSerializer(queryset, many=True)
    #     return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ViewSet):
    """ Category Model listing or retrieving """

    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
