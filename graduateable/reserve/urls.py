from django.urls import path
from . import views

urlpatterns = [
    path('', views.reserve, name='reserve'), 
    path('update/', views.ReserveView.as_view(), name='reserve-update'),
    path('get/',views.get_reverse, name='reserve-get')
]