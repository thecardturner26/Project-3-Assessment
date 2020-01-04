from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('add/', views.ItemCreate.as_view(), name='items_create'),
]