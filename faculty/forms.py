from django import forms
from .models import exam_name

class ExamForm(forms.ModelForm):
    class Meta:
        model = exam_name
        fields = '__all__'
        widgets = {
            'exam': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Exam Name'}),
            'center_incharge': forms.NumberInput(attrs={'class': 'form-control'}),
            'gtu_co': forms.NumberInput(attrs={'class': 'form-control'}),
            'sr_sup': forms.NumberInput(attrs={'class': 'form-control'}),
            'jr_sup': forms.NumberInput(attrs={'class': 'form-control'}),
            'st_sup': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_sup': forms.NumberInput(attrs={'class': 'form-control'}),
            'peon': forms.NumberInput(attrs={'class': 'form-control'}),
            'st_peon': forms.NumberInput(attrs={'class': 'form-control'}),
            'sweeper': forms.NumberInput(attrs={'class': 'form-control'}),
            'page_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }
