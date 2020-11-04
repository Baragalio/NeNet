from django.contrib.auth.models import User
from django import forms
from .models import Information
from . import choices

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Имя пользователя")
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', )


    def clean_password2(self):
        data = self.cleaned_data
        if data['password1'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return data['password2']


class InformationForm(forms.ModelForm):
    age = forms.ChoiceField(label="Возраст", choices=choices.AGES)
    gender = forms.ChoiceField(widget=forms.RadioSelect, label="Пол", choices=choices.GENDERS)
    color = forms.ChoiceField(widget=forms.RadioSelect, label="Любимый цвет", choices=choices.COLORS)
    season = forms.ChoiceField(widget=forms.RadioSelect, label="Любимое время года", choices=choices.SEASONS)
    scope = forms.ChoiceField(widget=forms.RadioSelect, label="Сфера деятельности", choices=choices.SCOPES)
    purpose = forms.ChoiceField(widget=forms.RadioSelect, label="Самая частая цель посещения интернета",\
                                choices=choices.PURPOSES)
    count_fr = forms.ChoiceField(widget=forms.RadioSelect, label="Количество друзей в соц. сетях",\
                                 choices=choices.COUNTS)

    class Meta:
        model = Information
        fields = ('age', 'gender', 'color', 'season', 'scope', 'purpose', 'count_fr')

