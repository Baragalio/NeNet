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
    color = forms.ChoiceField(label="Любимый цвет", choices=choices.COLORS)
    season = forms.ChoiceField(widget=forms.RadioSelect, label="Любимое время года", choices=choices.SEASONS)
    scope = forms.ChoiceField(widget=forms.RadioSelect, label="Сфера деятельности", choices=choices.SCOPES)
    purpose = forms.ChoiceField(widget=forms.RadioSelect, label="Самая частая цель посещения интернета",\
                                choices=choices.PURPOSES)
    count_fr = forms.ChoiceField(widget=forms.RadioSelect, label="Количество друзей в соц. сетях",\
                                 choices=choices.COUNTS)
    choice1 = forms.ChoiceField(widget=forms.RadioSelect(), label="Какой вариант вам нравится больше?", \
                                choices=choices.CHOICES1)
    choice2 = forms.ChoiceField(widget=forms.RadioSelect, label="Какой вариант вам нравится больше?", \
                                choices=choices.CHOICES2)
    choice3 = forms.ChoiceField(widget=forms.RadioSelect, label="Какой вариант вам нравится больше?", \
                                choices=choices.CHOICES3)
    choice4 = forms.ChoiceField(widget=forms.RadioSelect, label="Какой вариант вам нравится больше?", \
                                choices=choices.CHOICES4)
    choice5 = forms.ChoiceField(widget=forms.RadioSelect, label="Какой вариант вам нравится больше?", \
                                choices=choices.CHOICES5)
    theme = forms.ChoiceField(widget=forms.RadioSelect, label="Какая тема (цветовое оформление) вам нравится больше?",\
            choices=choices.THEMES)
    font = forms.ChoiceField(widget=forms.RadioSelect, label="Какой вариант шрифта вы предпочитаете?", \
                              choices=choices.FONTS)
    pref = forms.ChoiceField(widget=forms.RadioSelect, label="Какой вариант вам нравится больше?", \
            choices=choices.PREFS)
    pref2 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label="Что вы хотите видеть в меню на главном экране?",\
            choices=choices.PREFS2)
    #widget=forms.CheckboxSelectMultiple
    class Meta:
        model = models.Information
        fields = ('age', 'gender', 'color', 'season', 'scope', 'purpose', 'count_fr','choice1',\
                  'choice2','choice3','choice4','choice5','theme', 'pref', 'pref2')