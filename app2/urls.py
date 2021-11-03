from django.urls import path
from .views import HomePageView2, AboutPageView2

urlpatterns = [
    path('home2/', HomePageView2.as_view(), name='home2'),
    path('about2/', AboutPageView2.as_view(), name='about2'),
]
