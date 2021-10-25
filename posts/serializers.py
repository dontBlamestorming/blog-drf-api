from rest_framework import serializers
from .models import Category, Post


class PostListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'sub_title', 'thumbnail_url', 'category')

    """
        def to_representation(self, instance):
            # present category by name, not id
            rep = super().to_representation(instance)
            rep['category'] = instance.category.name
            return rep
    """


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'post_date', 'content',)


class CategorySerializer(serializers.ModelSerializer):
    posts = PostListSerializer(read_only=True, many=True)

    class Meta:
        model = Category
        fields = '__all__'
