from django_filters import rest_framework as filters
from rest_framework import viewsets

from blog.models import Article, Category
from api.serializer import ArticleSerializer, CategorySerializer

class ArticleFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Article
        fields = ['title']


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_class = ArticleFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
