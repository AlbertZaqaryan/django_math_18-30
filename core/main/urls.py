from django.urls import path
from . import views

urlpatterns = [
    path('', views.math, name='math'),
    path('calculator/', views.calculator, name='calculator'),
    path('factorial/', views.factorial, name='factorial'),
    path('calculator/res/', views.add, name='res'),
    path('factorial/fact/', views.fact, name='fact'),


]