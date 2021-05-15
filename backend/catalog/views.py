from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategoryInstanceSerializer, CategorySerializer, GenresSerializer, AuthorSerializer
from .models import CategoryInstance, Category, Genres, Author

class CategoryInstanceView(viewsets.ModelViewSet):
  serializer_class = CategoryInstanceSerializer
  queryset = CategoryInstance.objects.all()

class CategoryView(viewsets.ModelViewSet):
  serializer_class = CategorySerializer
  queryset = Category.objects.all()

class GenresView(viewsets.ModelViewSet):
  serializer_class = GenresSerializer
  queryset = Genres.objects.all()

class AuthorView(viewsets.ModelViewSet):
  serializer_class = AuthorSerializer
  queryset = Author.objects.all()
