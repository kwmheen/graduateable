from django.urls import path
from . import views

urlpatterns = [
    path('show-image/', views.show_image, name='show_image'),
    path('menu/', views.menu, name='menu'),
]