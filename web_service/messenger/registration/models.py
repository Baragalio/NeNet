from django.db import models
from django.conf import settings

class Information(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, verbose_name="Color", default='1')
    age = models.CharField(max_length=2, verbose_name="Age", default='1')
    gender = models.CharField(max_length=2, verbose_name="Gender", default='1')
    season = models.CharField(max_length=2, verbose_name="Season", default='1')
    sсope = models.CharField(max_length=2, verbose_name="Scope", default='1')
    purpose = models.CharField(max_length=2, verbose_name="Purpose", default='1')
    count_fr = models.CharField(max_length=2, verbose_name="Count_friends", default='1')
    choice1 = models.CharField(max_length=2, verbose_name="Choice1", default='1')
    choice2 = models.CharField(max_length=2, verbose_name="Choice2", default='1')
    choice3 = models.CharField(max_length=2, verbose_name="Choice3", default='1')
    choice4 = models.CharField(max_length=2, verbose_name="Choice4", default='1')
    choice5 = models.CharField(max_length=2, verbose_name="Choice5", default='1')
    theme = models.CharField(max_length=2, verbose_name="Theme", default='1')
    pref = models.CharField(max_length=2, verbose_name="Preference", default='1')
    pref2 = models.CharField(max_length=100, verbose_name="Preference_menu", default='1')
 
    def __str__(self):
        return 'Профиль пользователя {}'.format(self.user.username)