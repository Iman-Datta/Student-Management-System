from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='_home'),
    path('add/',views.add_stream, name='_add'),
]
