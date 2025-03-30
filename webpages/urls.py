from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homePage'),
    path('portfolio_details/', views.portfolio_details, name='homePage'),
    path('service_details/', views.service_details, name='homePage'),
    path('starter_page/', views.starter_page, name='homePage'),
]
