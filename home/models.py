from django.db import models

# Create your models here.

class admindb(models.Model):
    vno = models.CharField(max_length=50)
    oname = models.CharField(max_length=50)
    mname = models.CharField(max_length=50)
    mno = models.CharField(max_length=50)
    pyear = models.CharField(max_length=50)
    lno = models.CharField(max_length=50)
    foul = models.CharField(max_length=50)
    fine = models.CharField(max_length=50)
    oaddress = models.CharField(max_length=100)
    cdetail = models.CharField(max_length=50)
    lissuedate = models.CharField(max_length=50)
    lexpiredate = models.CharField(max_length=50)


class carmodel(models.Model):
    car_img = models.ImageField(upload_to = "car")
