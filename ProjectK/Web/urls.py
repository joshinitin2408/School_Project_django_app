from django.contrib import admin
from django.urls import path
from Web import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('facilities', views.facilities, name='facilities'),
    path('gallary', views.gallary, name='gallary'),
    path('infrastructure', views.infrastructure, name='infrastructure'),
    path('achievments', views.achievments, name='achievments'),
    path('admission', views.admission, name='admission'),
]