from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class Sso_Register(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,)
    sso_id = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)



