from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from customer.models import Orders
from owner.models import Mobile
class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","email","username","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(widget=forms.PasswordInput())

class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields=["address","qty"]
        widgets={
            "address":forms.Textarea(attrs={"class":"form-control"}),
            "qty":forms.NumberInput(attrs={"class":"form-control"})
            }

# class UpdateForm(forms.ModelForm):
#     class Meta:
#         model=Mobile
#         fields=["qty"]
#         widgets={
#             "mobile_name":forms.CharField(attrs={"class":"form-control"}),
#             "price":forms.NumberInput(attrs={"class":"form-control"})
#         }
