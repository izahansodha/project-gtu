from django import forms
from authenticate.models import custumuser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username','class':'mt-2 bg-transparent w-[197px] px-4 py-4 border-gray-500 rounded-lg'}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'full_name','class':'mt-2 bg-transparent w-[197px] px-4 py-4 border-gray-500 rounded-lg'}))
    role = forms.ChoiceField(choices=custumuser.ROLE_CHOICE,widget=forms.Select(attrs={'placeholder': 'username','class':'mt-2 bg-transparent w-[197px] px-4 py-4 border-gray-500 rounded-lg'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'mt-2 bg-transparent w-[197px] px-4 py-4 border-gray-500 rounded-lg'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'mt-2 bg-transparent w-[197px] px-4 py-4 border-gray-500 rounded-lg'}))

    class Meta:
        model = custumuser
        fields = ['username', 'full_name', 'role', 'password1', 'password2']




class CustomLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
