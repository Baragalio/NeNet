from django import forms

class LoginForm(forms.Forms):
    username = forms.CharField(label="Имя пользователя")
    password = forms.CharField(label="Пароль",widget=forms.PasswordInput)

