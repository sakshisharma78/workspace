from django.db import models

Create your models here.
class Username(models.Model):
    name=models.cherfield(max_length=255)
    date_of_birth=models.datetimefield()
    date_of_joining=models.datetimefield()
    address=models.textfield()
