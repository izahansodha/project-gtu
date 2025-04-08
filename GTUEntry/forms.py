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

        # Order exams in descending order by ID
        self.fields['exam_id'].queryset = exam_name.objects.all().order_by('-id')

        # Remove the default "---------" empty option
        self.fields['exam_id'].empty_label = None

        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'


class GTUExamCPForm(forms.ModelForm):
    class Meta:
        model = gtu_th_CP_data
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Order exams in descending order by ID
        self.fields['exam_id'].queryset = exam_name.objects.all().order_by('-id')

        # Remove the default "---------" empty option
        self.fields['exam_id'].empty_label = None

        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'
