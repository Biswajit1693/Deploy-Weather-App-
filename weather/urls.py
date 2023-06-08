from django.urls import path
from weather import views

urlpatterns = [
    #path('get_weather/' , views.get_weather ,name="get_weather"),
    path("" , views.get_weather, name="weather"),
    #path("/about", views.about, name="about")
]

