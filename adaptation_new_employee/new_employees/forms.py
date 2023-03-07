from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'name': 'username'}), required=True)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'name': 'psw'}), required=True)


class MissionsForm(forms.ModelForm):
    class Meta:
        model = MissionsModel
        fields = ['content', 'deadline', 'points']

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры!')
        return title
