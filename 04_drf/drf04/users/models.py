from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=80)
    password = models.CharField(max_length=80)

    class Meta:
        db_table = 't_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
