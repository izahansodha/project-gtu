from django import forms
from .models import exam_name, faculty, department


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
        labels = {
            'exam': 'Exam Period (SUMMER-2024)',
            'center_incharge': 'Center Incharge (Rs.)',
            'sr_sup': 'Senior Supervisor (Rs.)',
            'jr_sup': 'Junior Supervisor (Rs.)',
            'st_sup': 'Stationary Supervisor (Rs.)',
            'num_sup': 'Numbering Supervisor (Rs.)',
            'gtu_co': 'GTU Coordinator (Rs.)',
            'peon': 'Peon (Rs.)',
            'st_peon': 'Stationary Peon (Rs.)',
            'sweeper': 'Sweeper (Rs.)',
            'page_amount': 'Amount per Page (Rs.)',
        }


class FacultyForm(forms.ModelForm):
    class Meta:
        model = faculty
        fields = '__all__'
        widgets = {
            'pancard': forms.TextInput(attrs={'class': 'form-control'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'bank_name': forms.TextInput(attrs={'class': 'form-control'}),
            'account_no': forms.TextInput(attrs={'class': 'form-control'}),
            'ifsc': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Simply show all departments without filtering
        self.fields['department'].queryset = department.objects.all()


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = department
        fields = '__all__'
        widgets = {
            'department_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter department name'
            }),
        }