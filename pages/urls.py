from django.urls import path

from .views import homPage


urlpatterns = [
    path('', homPage, name = 'Home')
]

