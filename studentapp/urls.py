from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('addStudent/', views.add_student, name='add_student'),
    path('student_profile/<int:student_id>/', views.student_profile, name='student_profile'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('delete_student/<int:student_id>/', views.del_student, name='delete_student'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)