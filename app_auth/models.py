from django.db import models
from django.conf import settings
class Profile(models.Model):
    USERNAME_FIELD = 'username'
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length = 15)
    username = models.CharField(max_length=15)