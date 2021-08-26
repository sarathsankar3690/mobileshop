from django.urls import path
from owner import views

urlpatterns=[
    path("home",views.home,name="home"),
    path("mobiles/add",views.mobile_create,name="addmobile"),
    path("brands/add",views.brand_create,name="addbrand"),
    path("brands/search",views.brand_search,name="searchbrand"),
    path("brands/list",views.list_brand,name="listbrands"),
    path("brands/remove/<str:brand_name>",views.remove_brand,name="removebrand"),
    path("brands/edit/<str:brand_name>",views.update_brand,name="editbrand"),
    path("mobiles",views.mobile_list,name="listmobiles"),
    path("mobiles/change/<int:id>",views.mobile_update,name="editmobile"),
    path("mobiles/remove/<int:id>",views.remove_mobile,name="removemobile")


]