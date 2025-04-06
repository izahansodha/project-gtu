from django import forms
from .models import *
from faculty.models import *


class GTUExamDataForm(forms.ModelForm):
    class Meta:
        model = gtu_th_exam_data
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter only active faculty
        self.fields['faculty_id'].queryset = faculty.objects.filter(is_active=True)

