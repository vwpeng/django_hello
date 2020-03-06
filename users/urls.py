from django.conf.urls import url
from django.urls import path

from users import views

urlpatterns = [
    # 增加路由信息
    path('index/', views.index),
    url('hello/', views.hello),
]
