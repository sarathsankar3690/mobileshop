from django import forms
from django.forms import ModelForm
from .models import Mobile,Brand

class MobileCreationForm(ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"
        widgets={
            "mobile_name":forms.TextInput(attrs={'class':"form-control"}),
            "brand":forms.Select(attrs={'class':"form-select"}),
            "price":forms.TextInput(attrs={'class':"form-control"}),
            "os": forms.TextInput(attrs={'class': "form-control"}),
            "specs": forms.TextInput(attrs={'class': "form-control"}),
            "image": forms.FileInput(attrs={'class': "form-control"}),
        }

class BrandAddForm(ModelForm):
    class Meta:
        model=Brand
        fields="__all__"
        widgets={
            "brand_name":forms.TextInput(attrs={'class':"form-control"}),

        }
class BrandUpdateForm(ModelForm):
    class Meta:
        model=Brand
        fields="__all__"
        widgets={
            "brand_name":forms.TextInput(attrs={"class":'form-control'}),

        }

class BrandSearchForm(forms.Form):
        brand_name=forms.CharField(max_length=120,widget=forms.TextInput(attrs={"class":"form-control"}))

# class MobileUpdateForm(ModelForm):
#     class Meta:
#         model=Mobile
#         fields="__all__"
#         widgets={
#
#         }

class MobileUpdationForm(ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"
        widgets={
            "mobile_name":forms.TextInput(attrs={'class':"form-control"}),
            "brand":forms.Select(attrs={'class':"form-select"}),
            "price":forms.TextInput(attrs={'class':"form-control"}),
            "os": forms.TextInput(attrs={'class': "form-control"}),
            "specs": forms.TextInput(attrs={'class': "form-control"}),
        }
