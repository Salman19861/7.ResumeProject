from nturl2path import url2pathname
from unicodedata import name
from django.urls import path
from .import views
urlpatterns = [
    path('base/',views.base,name='base'),
    path('',views.home,name='home'),
    path('services/',views.services,name='services'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact')
]
