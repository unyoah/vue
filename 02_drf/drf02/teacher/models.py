from django.db import models


# Create your models here.
class Teacher(models.Model):
    gender_choices = (
        (0, 'male'),
        (1, 'female'),
        (2, 'other'),
    )
    name = models.CharField(max_length=80)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)
    phone = models.CharField(max_length=11, null=True, blank=True)

    class Meta:
        db_table = 't_teacher'
        verbose_name = '教师表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
