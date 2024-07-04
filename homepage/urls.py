from django.conf.urls import url
from django.urls import path,include
from homepage import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact/', views.contact, name='contact'),
    path ('about/',views.about,name='about'),
    
]
