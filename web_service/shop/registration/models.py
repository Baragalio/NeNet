from django.db import models
from django.conf import settings

class Information(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='information', on_delete=models.CASCADE)
    color = models.IntegerField(verbose_name="Color", default=0)
    age = models.IntegerField(verbose_name="Age", default=0)
    gender = models.IntegerField(verbose_name="Gender", default=0)
    season = models.IntegerField(verbose_name="Season", default=0)
    scope = models.IntegerField(verbose_name="Scope", default=0)
    purpose = models.IntegerField(verbose_name="Purpose", default=0)
    count_fr = models.IntegerField(verbose_name="Count_friends", default=0)
 
    def __str__(self):
        return 'Профиль пользователя {}'.format(self.user.username)