from django.urls import path

from . import views

urlpatterns = [
    path('', views.CartApi.as_view()),
]
