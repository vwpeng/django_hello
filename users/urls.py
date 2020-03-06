from django.urls import path

from users import views

urlpatterns = [
    # 增加路由信息
    path('index/', views.index),
    path('hello/', views.hello),
]
