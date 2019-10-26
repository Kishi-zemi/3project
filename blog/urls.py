from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='tab'),
    path('2016.html', views.sub1, name='2016'),
    path('2017.html', views.sub2, name='2017'),
    path('2018.html', views.sub3, name='2018'),
    path('all.html', views.sub4, name='all')
]
