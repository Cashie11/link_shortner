from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:short_code>/', views.redirect_original, name='redirect_original'),
]
