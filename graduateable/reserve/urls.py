from django.urls import path
from . import views

urlpatterns = [
    path('', views.reserve, name='reserve'), 
    path('update/', views.ReserveView.as_view(), name='reserve-update'),
    path('asdf/',views.update,name='asdf')
]