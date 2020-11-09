# 设置Django运行所依赖的环境变量
import json
import os

if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_book.drf_book.settings')

# 让Django进行一次初始化
import django

django.setup()

from rest_framework import serializers
from booktest.models import BookInfo, HeroInfo
from booktest.serializers import BookInfoSerializer, HeroInfoSerializer

if __name__ == '__main__':
    # 获取id为1的英雄数据
    hero = HeroInfo.objects.get(id=1)
    # 创建序列化器类
    serializer = HeroInfoSerializer(hero)
    res = serializer.data
    res = json.dumps(res, indent=1, ensure_ascii=False)
    print(res)

# if __name__ == '__main__':
#     books = BookInfo.objects.all()
#     # 创建序列化器对象
#     serializer = BookInfoSerializer(books, many=True)
#     res = serializer.data
#     res = json.dumps(res, indent=1, ensure_ascii=False)
#     print(res)
# if __name__ == '__main__':
#     book = BookInfo.objects.get(id=1)
#     # 创建序列
#     serializer = BookInfoSerializer(book)
#     # 获取序列化器后的数据
#     res = serializer.data
#     print(res)
