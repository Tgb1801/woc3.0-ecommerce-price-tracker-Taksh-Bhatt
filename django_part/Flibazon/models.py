from django.db import models

# Create your models here.


class User_Details(models.Model):
    website       = models.IntegerField()
    url           = models.URLField(max_length=100000)
    product_name  = models.TextField()
    Email_Id      = models.EmailField(max_length=5000)
    desired_price = models.FloatField()


class next_run_time(models.Model):
    time = models.DateTimeField()
