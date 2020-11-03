from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=11, unique=True)

    class Meta:
        db_table = 'api_uesr'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Computer(models.Model):
    name = models.CharField(max_length=80, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    brand = models.CharField(max_length=40)

    class Meta:
        db_table = "t_computer"
        verbose_name = "电脑"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
