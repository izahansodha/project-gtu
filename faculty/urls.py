from django.urls import path
from .views import *

urlpatterns = [
    path('add-exam/', add_exam, name='add_exam'),
    path('add-faculty/', add_faculty, name='add_faculty'),
    path('faculty-record/', faculty_list, name='faculty_list'),
    path('edit/<int:faculty_id>/', edit_faculty, name='edit_faculty'),
    path('department-record/', department_list, name='department_list'),
    path('add-department/', add_department, name='add_department'),
    path('edit/<int:dept_id>/', edit_department, name='edit_department'),
]