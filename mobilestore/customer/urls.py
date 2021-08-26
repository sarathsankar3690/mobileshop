from django.urls import path
from customer import views
urlpatterns=[
    path("accounts/signin",views.SignInView.as_view(),name="signin"),
    path("accounts/signup",views.RegistrationView.as_view(),name="signup"),
    # path("accounts/signout")
    path("home",views.CustomerHomeView.as_view(),name="customerhome"),
    path('productdetail/<int:id>',views.ProductDetailView.as_view(),name="productdetail"),
    path("products/addtocart/<int:id>",views.AddCartView.as_view(),name="addtocart"),
    path("products/cart/",views.ViewCart.as_view(),name="viewmycart"),
    path("products/removecart/<int:id>",views.RemoveCartView.as_view(),name="removecart"),
    path("products/placeorder/<int:c_id><int:p_id>",views.OrderView.as_view(),name="placeorder"),
    path("products/orders",views.MyOrders.as_view(),name="myorders")
]