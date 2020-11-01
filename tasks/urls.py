
from tasks.views import Smartphone
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('3dprinter', views.d3printer, name='3dprinter'),
    path('main_info', views.main_info, name='main_info'),
    path('Segway', views.Segway, name='Segway'),
    path('tablet', views.tablet, name='tablet'),
    path('VRAR', views.VRAR, name='VRAR'),
    path('Smartphone', views.Smartphone, name='Smartphone')
]
