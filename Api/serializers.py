from rest_framework import serializers
from .models import Article, ArticleDetail


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = '__all__'
        exclude = ['author',]  # 除了作者都进行验证


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleDetail
        exclude = ['article', ]