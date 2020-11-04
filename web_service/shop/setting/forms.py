from django import forms
from .models import MoreInformation
from . import choices


class MoreInformationForm(forms.ModelForm):
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
    theme = forms.ChoiceField(widget=forms.RadioSelect, label="Какая тема (цветовое оформление) вам нравится больше?", \
                              choices=choices.THEMES)
    font = forms.ChoiceField(widget=forms.RadioSelect, label="Какой вариант шрифта вы предпочитаете?", \
                             choices=choices.FONTS)
    pref = forms.ChoiceField(widget=forms.RadioSelect, label="Какой вариант вам нравится больше?", \
                             choices=choices.PREFS)
    pref2 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                      label="Что вы хотите видеть в меню на главном экране?", \
                                      choices=choices.PREFS2)
    class Meta:
        model = MoreInformation
        fields = ('choice1', 'choice2', 'choice3', 'choice4', 'choice5', 'theme', 'font', 'pref', 'pref2')
