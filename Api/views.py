from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet


from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArticleSerializer, ArticleDetailSerializer

class ArticleView(APIView):
    '''文章的视图类'''
    def get(self, request, *args, **kwargs):
        """获取文章"""
        return Response('qerea')

    def post(self, request, *args, **kwargs):
        """新增文章（应该在后台管理）"""
        data_dict = request.data

        serializer = ArticleSerializer(data=data_dict)
        serializer_detail = ArticleDetailSerializer(data=data_dict)
        validated = serializer.is_valid()
        if validated and serializer_detail.is_valid():
            print(request.data)
            article_object = serializer.save(author_id=1)
            serializer_detail.save(article_id=article_object.id)
        return Response('aaaaa')


class ArticleDetailView(ModelViewSet):
    pass













