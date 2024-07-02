from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView
from news_api.serializers import CategorySerializers,NewsSerializers
from news.models import Category, News

# Create your views here.

class CategoryViewSet (ListAPIView) :

    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class NewsViewSet(ListAPIView):

    queryset = News.objects.all()
    serializer_class = NewsSerializers

class NewsDetailView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers