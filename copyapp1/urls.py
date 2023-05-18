from django.urls import path
from . import views

app_name = 'copyapp1'
urlpatterns = [
    path('', views.index, name='index'),   # 一覧
]