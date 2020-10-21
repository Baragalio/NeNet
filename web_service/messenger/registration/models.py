from django.db import models
from django.conf import settings

class Information(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, verbose_name="Color", default=1)
    age = models.IntegerField(verbose_name="Age", default=1)
    gender = models.IntegerField(verbose_name="Gender", default=1)
    season = models.IntegerField(verbose_name="Season", default=1)
    sсope = models.IntegerField(verbose_name="Scope", default=1)
    purpose = models.IntegerField(verbose_name="Purpose", default=1)
    count_fr = models.IntegerField(verbose_name="Count_friends", default=1)
 
    def __str__(self):
        return 'Профиль пользователя {}'.format(self.user.username)