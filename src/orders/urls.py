from django.urls import path

from orders import views

urlpatterns = [
    path('', views.OrdersApi.as_view()),
]
