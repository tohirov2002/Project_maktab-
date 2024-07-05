from rest_framework import serializers
from .models import Categories, News


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class NewsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['news_title', 'news_description', 'news_image', 'news_content', 'pub_date', 'news_category', 'news_author']


class NewsVedioSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['news_title', 'news_description', 'news_vedio', 'news_content', 'pub_date', 'news_category', 'news_author']