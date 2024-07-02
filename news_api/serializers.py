from rest_framework import serializers
from news.models import Category, News


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class NewsSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    class Meta:
        model = News
        fields = '__all__'