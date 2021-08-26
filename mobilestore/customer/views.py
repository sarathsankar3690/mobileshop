from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.generic import TemplateView,DetailView,ListView,CreateView
from owner.models import Mobile
from customer.models import Cart,Orders
from django.contrib import messages
# Create your views here.

class RegistrationView(TemplateView):
    form_class=forms.RegistrationForm
    template_name = "registration.html"
    model = User
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            self.context={"form":form}
            return render(request,self.template_name,self.context)

class SignInView(TemplateView):
    template_name = "login.html"
    form_class = forms.LoginForm
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("customerhome")
            else:
                self.context={"form":form}
                return render(request,self.template_name,self.context)

class CustomerHomeView(ListView):
    template_name = "customerhome.html"
    model = Mobile
    context_object_name = "mobiles"

class ProductDetailView(DetailView):
    model = Mobile
    template_name = "productdetails.html"
    context_object_name = "mobile"
    pk_url_kwarg = 'id'

class AddCartView(TemplateView):
    model=Cart
    def get(self,request,*args,**kwargs):
        product_id=kwargs["id"]
        product=Mobile.objects.get(id=product_id)
        user=request.user
        cart=Cart(product=product,user=user)
        cart.save()
        messages.success(request,"added to cart")
        return redirect("customerhome")

class ViewCart(ListView):
    model=Cart
    template_name = "cartitems.html"
    context_object_name = "items"
    def get_queryset(self):
        queryset=self.model.objects.filter(user=self.request.user)
        return queryset

class RemoveCartView(TemplateView):
    model=Cart
    def get(self,request,*args,**kwargs):
        product_id=kwargs["id"]
        product=Cart.objects.get(id=product_id)
        product.delete()
        return redirect("viewmycart")

class OrderView(CreateView):
    template_name = "orderplace.html"
    form_class = forms.OrderForm
    model=Orders
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            cart_id=kwargs["c_id"]
            product_id=kwargs["p_id"]
            cart=Cart.objects.get(id=cart_id)
            product=Mobile.objects.get(id=product_id)
            order.product=product
            order.user=request.user
            order.save()
            cart.status="order_placed"
            cart.save()
            return redirect("customerhome")

class MyOrders(ListView):
    template_name = "myorders.html"
    context_object_name = "orders"
    model=Orders

    def get_queryset(self):
        queryset=self.model.objects.filter(user=self.request.user,status="in_cart")
        return queryset

# class UpdateCartView(TemplateView):
#     template_name = "updatecart.html"
#     form_class=forms.UpdateForm
#     model=Mobile
#     def post(self,request,*args,**kwargs):
#         form=self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
