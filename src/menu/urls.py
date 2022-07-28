from django.urls import path

from . import views

urlpatterns = [
    path('', views.MenuListApi.as_view()),
]
