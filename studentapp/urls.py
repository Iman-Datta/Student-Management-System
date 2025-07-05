from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='_home'),
    path('add/',views.create, name='_add'),
    path('retrieve/',views.retrieve, name='_retrieve'),
    path('delete/',views.delete, name='_delete'),
    path('update/',views.update, name='_update'),
]