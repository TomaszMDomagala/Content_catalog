from .models import Genres, Author, CategoryInstance, Category
from rest_framework import serializers

class GenresSerializer(serializers.ModelSerializer):
  class Meta:
    model = Genres
    fields = ('name', )

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = ('first_name', 'last_name', 'pseudonym', 'date_of_birth', 'date_of_death')

class CategorySerializer(serializers.ModelSerializer):
  author = AuthorSerializer()
  genre = GenresSerializer(many=True)

  class Meta:
    model = Category
    fields = ('title', 'author', 'year', 'link', 'genre', 'image', 'media_type')

class CategoryInstanceSerializer(serializers.ModelSerializer):
  category = CategorySerializer()

  class Meta:
    model = CategoryInstance
    fields = ('id', 'category', 'rating')