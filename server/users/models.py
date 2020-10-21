from django.db import models


# Create your models here.


class Users(models.Model):
    userId = models.CharField(verbose_name='userId', max_length=20)
    sex = models.CharField(verbose_name='gender', default='male', max_length=20)
    phone = models.IntegerField(verbose_name='phone')
    password = models.CharField(verbose_name='password', max_length=20)

    class Meta:
        verbose_name = "user list"
        verbose_name_plural = verbose_name
