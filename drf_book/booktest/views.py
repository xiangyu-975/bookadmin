from booktest.models import BookInfo
from rest_framework.viewsets import ModelViewSet
from booktest.serializers import BookInfoSerializer


# 使用DRF框架，实现图书管理的5个接口
class BookInfoViewSet(ModelViewSet):
    '''视图集'''
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
