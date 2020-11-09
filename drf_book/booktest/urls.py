from booktest import views
from rest_framework.routers import DefaultRouter

urlpatterns = [

]

# 路由Router：动态生成视图集中处理函数的url配置项

router = DefaultRouter()  # 路由router
router.register('books', views.BookInfoViewSet, basename='books')  # 向路由router中注册视图集
urlpatterns += router.urls  # 将路由Router生成的url配置信息添加到django的路由列表中
