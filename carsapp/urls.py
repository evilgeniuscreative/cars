
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


path('cars/', views.CarsList.as_view(), name='cars_list'),
path('cars/<int:pk>', views.CarsDetail.as_view(), name="cars_detail")