from django.urls import path
from . import views

urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('python/', views.python, name='python'),
    path('cpp/', views.cpp, name='cpp'),
    path('web_layout/', views.web_layout, name='web_layout'),
    path('devops/', views.devops, name='devops'),
    path('java/', views.java, name='java')
]