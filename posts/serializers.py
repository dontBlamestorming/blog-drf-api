from rest_framework import serializers
from .models import Category, Post


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
