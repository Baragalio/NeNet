from django.db import models
from django.conf import settings

class Information(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, verbose_name="Любимый цвет")
 
    def __str__(self):
        return 'Профиль пользователя {}'.format(self.user.username)