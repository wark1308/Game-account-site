from rest_framework import serializers
from .models import *



class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('author', 'title', 'picture', 'info', 'money', 'id')


class GameDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('author', 'title', 'picture', 'info', 'money', 'id')


# class GameDeleteSerializer(serializers.ModelSerializer):


# class GameUpdateSerializer(serializers.ModelSerializer):


class GameCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'picture', 'info', 'money')

    def create(self, validated_data):
        author = self.context.get('author')
        game = Post.objects.create(author=author, **validated_data)
        game.save()
        return game