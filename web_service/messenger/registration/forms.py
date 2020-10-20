from django.contrib.auth.models import User
from django import forms
from . import models

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return data['password2']

class InformationForm(forms.ModelForm):
    color = forms.CharField(max_length=20, label="Favorite color")

    class Meta:
        model = models.Information
        fields = ('color',)