from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from datetime import datetime

# Create your models here.

# class User(AbstractUser):
#     email=models.EmailField(unique=True)
#     verified_at = models.CharField(max_length=200,default='True')
#     role =models.CharField(max_length=200,default='user')
#     status = models.CharField(max_length=20, default='1')
#     updated_at = models.CharField(max_length=200,default=datetime.utcnow())
#     created_at = models.CharField(max_length=200,default=datetime.utcnow())
#     remember_token=models.CharField(max_length=200,null=True)

class Login(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=150, blank=True, null=True)  # Field name made lowercase.
    user_type = models.CharField(db_column='User_Type', max_length=50, blank=True, null=True)  # Field name made lowercase.
    f_name = models.CharField(db_column='F_NAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    l_name = models.CharField(db_column='L_NAME', max_length=150, blank=True, null=True)  # Field name made lowercase.
    approval = models.CharField(db_column='APPROVAL', max_length=150, blank=True, null=True)  # Field name made lowercase.
    # dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    # mobile = models.CharField(db_column='MOBILE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    # email = models.CharField(db_column='EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    # address = models.CharField(db_column='ADDRESS', max_length=250, blank=True, null=True)  # Field name made lowercase.
    # profile_photo = models.CharField(db_column='PROFILE_PHOTO', max_length=250, blank=True, null=True)  # Field name made lowercase.
    # crt_date = models.DateTimeField(db_column='CRT_DATE', blank=True, null=True)  # Field name made lowercase.
    # image = models.ImageField(upload_to=filepath, null=True, blank=True)
    # passwordstatus  = models.CharField(db_column='passwordchange', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # activation = models.CharField(db_column='activation', max_length=100, blank=True, null=True)  
    