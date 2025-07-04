from django.contrib import admin
from django.urls import path, include
from .views import home_view, gen_view, contact_view, about_view

urlpatterns = [
    path('', home_view, name='home'),
    path('generator', gen_view, name='gen'),
    path('contact-us', contact_view, name='contact-us'),
    path('about-us', about_view, name='about-us')

]