from calendar import c
from functools import update_wrapper

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.base import Model
from django.db.models.fields import EmailField
from django.db.models.deletion import SET_NULL
from django.forms import ModelForm
from django import forms
from datetime import datetime, timedelta


class Kategorije(models.Model):
    kategorija=models.CharField(max_length=100)

class Periferija_i_memorija(models.Model):
    periferija_i_memorija=models.CharField(max_length=100)
    
class Computers(models.Model):
    naziv=models.CharField(max_length=50)
    opis=models.TextField()
    slika=models.ImageField(upload_to="static/img_artikli")
    slika2=models.ImageField(upload_to="static/img_artikli") 
    slika3=models.ImageField(upload_to="static/img_artikli")
    slika4=models.ImageField(upload_to="static/img_artikli")
    datum_objave=models.DateField(auto_now_add=True)
    cijena=models.DecimalField(max_digits=9 , decimal_places=2)
    izdvojen=models.CharField(max_length=10)
    id_kategorija=models.IntegerField(null=True)
    id_podkategorija=models.IntegerField(null=True)


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have email")
        
        if not username:
            raise ValueError("User must have username")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
# Create your models here.

def get_profile_image_filepath(self):
    return f'images/{str(self.pk)}/{"profile_image.png"}'

def get_defaultimg():
    return "images/default.png"
    

class Account(AbstractBaseUser):
    email = EmailField(verbose_name="email",max_length=60, unique=True)
    username = models.CharField(max_length=45)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath,  null = True, blank = True, default=get_defaultimg)
    gender = models.CharField(max_length=45)
    hide_email = models.BooleanField(default=True)
    address = models.CharField(max_length=45,  null = True)
    number = models.IntegerField(null=True)



    objects = MyAccountManager()
    #postavljanje e maila za defoltni login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username
    
    def get_image_name(self):
        return str(self.profile_image)[str(self.profile_image).index(f'images/{self.pk}/'):]

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_Lable):
        return True

class SlideShow(models.Model):
    slika1=models.ImageField(upload_to="static/img_slideShow") 
    slika2=models.ImageField(upload_to="static/img_slideShow")
    slika3=models.ImageField(upload_to="static/img_slideShow")
    


class ShopCart(models.Model):
    id_proizvod = models.IntegerField(null=True)
    id_customer = models.CharField(max_length=45,null=True)
    date_start = models.DateTimeField(default=datetime.now()+timedelta(days=1))
    kolicina = models.IntegerField(default=1)
    iznos = models.IntegerField(null=True)

class Reklama1(models.Model):
    slika1=models.ImageField(upload_to="static/reklama1") 
    slika2=models.ImageField(upload_to="static/reklama1")
    slika3=models.ImageField(upload_to="static/reklama1")

class Reklama2(models.Model):
    slika1=models.ImageField(upload_to="static/reklama2") 
    slika2=models.ImageField(upload_to="static/reklama2")
    slika3=models.ImageField(upload_to="static/reklama2")



  


class Customer(models.Model):
    email = EmailField(max_length=60)
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    address = models.CharField(max_length=45,  null = True)
    number = models.CharField(max_length=100 ,  null = True)
    id_customer = models.CharField(max_length=100 ,  null = True)
    cijena = models.IntegerField(null=True)
    proizvodi = models.CharField(max_length=1145,  null = True)
    date_start_pay = models.DateTimeField(default=datetime.now()+timedelta(days=1))


class Kmesages (models.Model):
    name = models.CharField(max_length=45)
    email = EmailField(max_length=60)
    kmessages = models.TextField(max_length=500)
