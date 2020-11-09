import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from drf_book.booktest.models import BookInfo


# Create your views here.

# 1. 获取所有的图书数据
# 2. 新增一本图书数据
# 3. 获取指定的图书数据
# 4. 修改指定的图书数据
# 5. 删除指定的图书数据

# /books/


class BookListView(View):
    def get(self, request):
        '''获取所有图书数据'''
        # 获取所有书的数据
        books = BookInfo.objects.all()  # QuerySet
        # 将所有的书的数据通过json进行返回
        books_li = []
        for book in books:
            book_dict = {
                'id': book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment
            }
            books_li.append(book_dict)
        return JsonResponse(books_li, safe=False)

    def post(self, request):
        '''
        新增一本图书
        获取参数并校验(参数完整性，日期格式)
        利用数据新增图书
        新增图书json返回
        '''
        req_data = request.body  # bytes
        json_str = req_data.decode()  # str
        req_dict = json.loads(json_str)
        # 获取参数
        btitle = req_dict.get('btitle')
        bpub_date = req_dict.get('bpub_date')
        # TODO:省略了参数的校验过程
        # 利用数据新增图书数据并保存到数据库中
        book = BookInfo.objects.create(btitle=btitle, bpub_date=bpub_date)
        # 将新增的图书数据通过json数据进行返回
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
        }
        return JsonResponse(book_dict, status=201)


# /books/(?P<pk>\d+)/
class BookDetailView(View):
    def get(self, request, pk):
        '''获取指定图书的数据'''
        # 根据pk获取对应的图书
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)
        # 将图书的数据转为json进行返回
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
        }
        return JsonResponse(book_dict)

    def put(self, request, pk):
        '''修改图书的数据'''
        # 1. 根据pk获取指定的图书数据
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)
        # 2. 获取参数并进行校验（参数完整性，日期格式）
        req_data = request.body  # bytes
        json_str = req_data.decode()  # str
        req_dict = json.loads(json_str)
        # 获取参数
        btitle = req_dict.get('btitle')
        bpub_date = req_dict.get('bpub_date')
        # TODO: 校验过程省略
        # 3. 修改指定图书并保存到数据库
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()
        # 4. 将修改的图书数据通过json进行返回
        book_dict = {
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
        }
        return JsonResponse(book_dict)

    def delete(self, request, pk):
        '''删除指定图书数据'''
        # 根据pk获取图书数据
        try:
            book = BookInfo.objects.get(id=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)
        # 删除图书数据
        book.delete()
        # 返回响应
        return HttpResponse(status=204)

