from django.shortcuts import render,redirect
from .forms import MobileCreationForm,MobileUpdationForm,BrandAddForm,BrandUpdateForm,BrandSearchForm
from .models import Brand,Mobile
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,"home.html")


def mobile_create(request):
    context={}
    form=MobileCreationForm()
    context["form"]=form
    if request.method=="POST":
        form=MobileCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"mobile created")
        else:
            messages.error(request,"mobile can't be added")
            context["form"]=form
            return render(request,"mobile_create.html",context)


    return render(request,"mobile_create.html",context)

def mobile_list(request):
    mobiles=Mobile.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"mobile_list.html",context)

def mobile_update(request,id):
    mobile=Mobile.objects.get(id=id)
    form=MobileUpdationForm(instance=mobile)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=MobileUpdationForm(instance=mobile,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listmobiles")
        else:
            context={}
            context["form"]=form
            return render(request, "mobile_edit.html", context)

    return render(request,"mobile_edit.html",context)

def mobile_detail(request,id):
    mobile=Mobile.objects.get(id=id)
    context={}
    context["mobiles"]=mobile
    return render(request,"mobile_detail.html",context)

def remove_mobile(request,id):
    mobile=Mobile.objects.get(id=id)
    mobile.delete()
    return render(request,"mobile_list.html")



def brand_create(request):
    context={}

    form=BrandUpdateForm
    if request.method=="GET":
        context["form"]=form
        return render(request,"brand_create.html",context)
    if request.method=="POST":
        form=BrandUpdateForm
        if form.is_valid():
            form.save()
            return redirect("addbrand")
        else:
            context["form"]=form
            return render(request,"brand_create.html",context)

def brand_search(request):
    brands=Brand.objects.all()
    context={}
    context["brand"]=brands
    form=BrandSearchForm(request.POST)
    context["form"]=form
    if request.method=="POST":
        form=BrandSearchForm(request.POST)
        if form.is_valid():
            brand_name=form.cleaned_data["brand_name"]
            brands=Brand.objects.filter(brand_name=brand_name)
            context["brand"]=brands
            return render(request,"brand_list.html",context)
        else:
            context["form"]=form
            return render(request,"brand_list.html",context)

    return render(request, "brand_list.html", context)

def list_brand(request):
    brands=Brand.objects.all()
    context={}
    context["brand"]=brands
    form=BrandAddForm()
    context["form"]=form
    if request.method=="POST":
        form=BrandAddForm(request.POST)
        if form.is_valid():
            brand_name=form.cleaned_data["brand_name"]
            brand=Brand.objects.filter(brand_name__contains=brand_name)
            context["brand"]=brand
            return render(request,"brand_list.html",context)
        else:
            context["form"]=form
            return render(request,"brand_list.html",context)

    return render(request,"brand_list.html",context)



def remove_brand(request,brand_name):
    brand=Brand.objects.get(brand_name=brand_name)
    brand.delete()
    return redirect("searchbrand")

def update_brand(request,id):
    brand=Brand.objects.get(id=id)
    form=BrandAddForm(instance=brand)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BrandAddForm(instance=brand,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("listbrands")
        return render(request,"brand_update.html",context)
