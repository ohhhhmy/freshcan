from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('fpost/', views.fpost, name = 'fpost'),
    path('fshow/', views.fshow, name='fshow'),
    path('home/', views.home, name='homw'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]