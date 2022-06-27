from . import views
from django.urls import path


urlpatterns = [
    path('create/', views.order_create, name='order_create'),
]