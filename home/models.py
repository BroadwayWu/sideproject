from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Members(models.Model):
    account = models.CharField(max_length=30,null=False)
    password = models.CharField(max_length=30,null=False)
    useremail = models.EmailField(max_length=30,null=False)
    gender = models.CharField(max_length=5,null=False)
    userbirth = models.DateField(null=False)
    career = models.CharField(max_length=10,null=False)
    resident = models.CharField(max_length=5,null=False)
    received_mail = models.CharField(max_length=5,null=False)
    
    class Meta:
        db_table = "members"


class StoryMap(models.Model):
    RowNumber = models.TextField()
    REF_WP = models.TextField()
    CAT1 = models.TextField()
    CAT2 = models.TextField()
    MEMO_TIME = models.TextField()
    SERIAL_NO = models.TextField()
    stitle = models.TextField()
    xbody = models.TextField()
    xurl = models.TextField()
    idpt = models.TextField()
    address = models.TextField()
    fileurl = models.TextField()
    info = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    MRT = models.TextField()

    class Meta:
        db_table = "storymap"


class Survey_Outcome(models.Model):
    account = models.CharField(max_length=30,null=False)
    Question1 = models.CharField(max_length=20,null=False)
    Question2 = models.CharField(max_length=20,null=False)
    Question3 = models.CharField(max_length=20,null=False)
    Question4 = models.CharField(max_length=20,null=False)
    Question5 = models.CharField(max_length=20,null=False)
    Question6 = models.CharField(max_length=20,null=False)
    Question6 = models.CharField(max_length=20,null=False)
    Question7 = models.CharField(max_length=200)

    class Meta:
        db_table = "survey_outcome"