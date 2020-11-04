from django.db import models
from django.conf import settings

class MoreInformation(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='more_information', on_delete=models.CASCADE)
    choice1 = models.IntegerField(verbose_name='choice1', default=0)
    choice2 = models.IntegerField(verbose_name='choice2', default=0)
    choice3 = models.IntegerField(verbose_name='choice3', default=0)
    choice4 = models.IntegerField(verbose_name='choice4', default=0)
    choice5 = models.IntegerField(verbose_name='choice5', default=0)
    theme = models.IntegerField(verbose_name='theme', default=0)
    pref = models.IntegerField(verbose_name='pref', default=0)

    def __str__(self):
        return 'Дополнительная информация о пользователе {}'.format(self.user.username)