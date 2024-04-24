from django.urls import path

from . import views

urlpatterns = [
 
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about-us/', views.about, name='about-us'),
    path('blog-grid-sidebar/', views.service, name='blog-grid-sidebar'),
]
