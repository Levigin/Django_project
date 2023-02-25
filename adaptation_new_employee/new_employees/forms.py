from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'name': 'username'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'name': 'psw'}), required=True)


# class MissionsBossForm(forms.ModelForm):
#     class Meta:
#         model = MissionsBoss
#         fields = ['title', 'deadline', 'point']
#
#     def clean_title(self):
#         title = self.cleaned_data['title']
#         if re.match(r'\d', title):
#             raise ValidationError('Название не должно начинаться с цифры!')
#         return title
#
#
# class MissionsHRForm(forms.ModelForm):
#     class Meta:
#         model = MissionsHR
#         fields = ['title', 'deadline', 'point']
#
#     def clean_title(self):
#         title = self.cleaned_data['title']
#         if re.match(r'\d', title):
#             raise ValidationError('Название не должно начинаться с цифры!')
#         return title
