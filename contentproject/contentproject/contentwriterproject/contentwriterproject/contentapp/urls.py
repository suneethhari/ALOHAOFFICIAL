from . import views
from django.urls import path

app_name='contentapp'


urlpatterns = [
    path('',views.demo,name='demo'),
    path('about/',views.about,name='about'),
    path('gallery/',views.gallery,name='gallery'),
    path('contact/',views.contact,name='contact'),
    path('single/',views.single,name='single')
]

