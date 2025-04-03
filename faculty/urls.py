from django.urls import path
from .views import add_exam

urlpatterns = [
    path('add-exam/', add_exam, name='add_exam'),
]
