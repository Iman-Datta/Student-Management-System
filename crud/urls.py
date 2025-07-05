from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.home, name='_home'),
    # path('add', views.add, name='_add')
    path('',include('studentapp.urls'))         # this is the way of including an app
   
]
