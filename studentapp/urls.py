from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('addStudent/', views.add_student, name='add_student'),
    path('student_profile/<int:student_id>/', views.student_profile, name='student_profile'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
]