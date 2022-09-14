from django.db import models
from django.contrib.auth.models import User


class Instructor(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile_phone = models.CharField(max_length=50, verbose_name='Mobile Phone')
    dob = models.DateField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=30)

    def __str__(self):
        return self.user.username
