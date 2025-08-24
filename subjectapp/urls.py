from django.urls import path
from . import views

urlpatterns = [
    path('', views.subject_list, name='subject_list'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('update_subject/<int:subject_id>/', views.edit_subject, name='update_subject'), 
    path('del_subject/<int:subject_id>/', views.del_subject, name='del_subject'),
]


# Query parameter => update_subject/<int:subject_id>/'