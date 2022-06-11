from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.index, name='home'),
    path('adminright',views.adminright, name='adminright'),
    path('display',views.display, name='display'),
    path('carimg',views.carimg,name='carimg')

]