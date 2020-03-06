from django.urls import path

from router import views

urlpatterns = [
    # 增加路由信息
    path('routerv/', views.routerv),
]
