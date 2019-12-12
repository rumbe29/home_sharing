from django.contrib import admin
from django.urls import path, include

from apps.rent.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('d/', HomeView.as_view(), name='home')
]