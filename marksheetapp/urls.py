from django.urls import path
from . import views

urlpatterns = [
    path('', views.marksheet_list, name='marksheet_list'),
    path('add_markSheet', views.add_marksheet, name="")
]