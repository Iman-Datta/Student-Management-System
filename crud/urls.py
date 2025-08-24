from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='_home'),
    path('stream/',include('streamapp.urls')), 
    path('subject/',include('subjectapp.urls'))  
   
]


# localhost:8000/stream/
