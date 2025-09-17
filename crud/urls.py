from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='_home'),
    path('stream/',include('streamapp.urls')), 
    path('subject/',include('subjectapp.urls')),
    path('student/',include('studentapp.urls')),
    path('marksheet/', include('marksheetapp.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# localhost:8000/stream/
