# from django import forms
# from authenticate.models import custumuser
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth import get_user_model
#
#
# class CustomUserCreationForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username','class':'form-control'}))
#     full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'full_name','class':'form-control '}))
#     role = forms.ChoiceField(choices=custumuser.ROLE_CHOICE,widget=forms.Select(attrs={'placeholder': 'username','class':'form-control'}))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}))
#
#     class Meta:
#         model = custumuser
#         fields = ['username', 'full_name', 'role', 'password1', 'password2']
#
# class CustomUserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = custumuser
#         fields = ['username', 'full_name', 'role']  # Fields to edit
#
#     def __init__(self, *args, **kwargs):
#         super(CustomUserUpdateForm, self).__init__(*args, **kwargs)
#
#         # Add Bootstrap classes to form fields
#         for field_name, field in self.fields.items():
#             field.widget.attrs.update({
#                 'class': 'form-control',  # Bootstrap form control styling
#                 'placeholder': field.label  # Placeholder text
#             })
#
#
# class CustomLoginForm(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
#
#
# User = get_user_model()  # Get the custom user model
#
# class AdminPasswordChangeForm(forms.Form):
#     new_password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'}),
#         label="New Password"
#     )
#     confirm_password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
#         label="Confirm Password"
#     )
#
#     def __init__(self, *args, **kwargs):
#         self.user = kwargs.pop('user', None)  # Get the user instance
#         super(AdminPasswordChangeForm, self).__init__(*args, **kwargs)
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("new_password")
#         confirm_password = cleaned_data.get("confirm_password")
#
#         if password != confirm_password:
#             raise forms.ValidationError("Passwords do not match.")
#
#         return cleaned_data
#
#     def save(self):
#         self.user.set_password(self.cleaned_data["new_password"])
#         self.user.save()
