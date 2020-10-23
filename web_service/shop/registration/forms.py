from django.contrib.auth.models import User
from django import forms
from . import models
from . import choices

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
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
        model = models.Information
        fields = ('age', 'gender', 'color', 'season', 'scope', 'purpose', 'count_fr')