from django.urls import path
from . import views

urlpatterns = [
    path('exam-th-entry/', views.exam_data_view, name='exam_data'),
    path('load-times/', views.load_times, name='load_times'),
    path('load-faculty/', views.load_faculty, name='load_faculty'),
    # path('view-exam/', views.exam_entry, name='exam_entry'), #not required
    path('exam-views/', views.exam_views, name='exam_views'),
    path('edit-exam/<int:exam_id>/', views.edit_exam, name='edit_exam'),
    path('add-exam-cp-data/', views.add_gtu_exam_cp, name='add_gtu_exam_cp'),
    path('cp-exams/', views.cp_exam_views, name='cp_exam_views'),
    path('cp-exams/edit/<int:cp_id>/', views.edit_cp_exam, name='edit_cp_exam'),
    #path('pdf-genrate/', views.exam_schedule_pdf_view, name='pdf_genrate'),
    path('pdf-selection/', views.select_pdf, name='select_pdf'),
    path('download-pdf/<int:faculty_id>/<int:exam_id>/',views.download_pdf , name='download_pdf'),
    path('select-exam/', views.select_exam_for_pdf, name='select_exam_for_pdf'),
    path('generate-all-pdfs/<int:exam_id>/', views.allpdf, name='generate_all_pdfs'),
    path('select-exam-excel/', views.select_exam_for_excel, name='select_exam_excel'),
    path('generate-excel/<int:exam_id>/', views.generate_excel, name='generate_excel'),
]
