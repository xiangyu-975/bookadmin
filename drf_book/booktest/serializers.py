from rest_framework import serializers
from booktest.models import BookInfo


class BookInfoSerializer(serializers.Serializer):
    '''序列化器类'''
    id = serializers.IntegerField(label='图书id', read_only=True)
    btitle = serializers.CharField(label='图书标题')
    bpub_date = serializers.DateField(label='出版日期')
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)


class HeroInfoSerializer(serializers.Serializer):
    '''序列化器类'''
    GENDER_CHOICES = (
        (0, '男'),
        (1, '女')
    )
    id = serializers.IntegerField(label='英雄id')
    hname = serializers.CharField(label='英雄名字')
    hgender = serializers.ChoiceField(label='性别',choices=GENDER_CHOICES)
    hcomment = serializers.CharField(label='备注')

