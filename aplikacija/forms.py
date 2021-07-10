from django import forms
import django
from django.contrib.auth import get_user_model

from .models import Account, Computers , SlideShow ,Reklama1,Reklama2,Customer,Kmesages 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate









class ProizvodForma(forms.ModelForm):
    slika = forms.ImageField(required=False)
    slika2 = forms.ImageField(required=False)
    slika3 = forms.ImageField(required=False)
    slika4 = forms.ImageField(required=False)
    id_podkategorija=forms.IntegerField(required=False)
    class Meta:
        model = Computers
        fields = [
            'naziv',
            'opis',
            'cijena',
            'slika',
            'slika2',
            'slika3',
            'slika4',
            'izdvojen',
            'id_kategorija',
            'id_podkategorija',
            
        ]

   
 




class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    class Meta:
        model = Account 
        fields = ("email", "username", "password1", "password2", "firstname", "lastname", "gender", "address","number")


class LoginAutentForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = Account
        fields = ('email', 'password')
    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email,password=password):
            raise forms.ValidationError("Invalid login")

       



class ShopSlide(forms.ModelForm):
    slika1 = forms.ImageField(required=False)
    slika2 = forms.ImageField(required=False)
    slika3 = forms.ImageField(required=False)
    class Meta:
        model = SlideShow
        fields = [
            'slika1',
            'slika2',
            'slika3',
]



class Reklam1(forms.ModelForm):
    slika1 = forms.ImageField(required=False)
    slika2 = forms.ImageField(required=False)
    slika3 = forms.ImageField(required=False)
    class Meta:
        model = Reklama1
        fields = [
            'slika1',
            'slika2',
            'slika3',
]


class Reklam2(forms.ModelForm):
    slika1 = forms.ImageField(required=False)
    slika2 = forms.ImageField(required=False)
    slika3 = forms.ImageField(required=False)
    class Meta:
        model = Reklama2
        fields = [
            'slika1',
            'slika2',
            'slika3',
]



class PayCart(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'id_customer',
            'email',
            'firstname',
            'lastname',
            'address',
            'number' ,
            'cijena',
            'proizvodi',
       
           
           
        ]


class Mesage(forms.ModelForm):
    class Meta:
        model = Kmesages 
        fields = [
            'name',
            'email',
            'kmessages',
           
           

        ]