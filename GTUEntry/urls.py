from django.urls import path
from . import views

urlpatterns = [
    path('exam-th-entry/', views.exam_data_view, name='exam_data'),
    path('load-times/', views.load_times, name='load_times'),
    path('load-faculty/', views.load_faculty, name='load_faculty'),
    path('view-exam/', views.exam_entry, name='exam_entry'),
    path('exam-views/', views.exam_views, name='exam_views'),
    path('edit-exam/<int:exam_id>/', views.edit_exam, name='edit_exam'),
]
