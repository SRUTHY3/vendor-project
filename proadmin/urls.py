
from django.contrib import admin
from django.urls import path 
from . import views
urlpatterns = [
  
    path("alogin",views.alogin,name="alogin"),
    path("ahome",views.ahome,name="ahome"),

# cater
    path("companylist",views.companylist,name="companylist"),
    path("mssglist",views.mssglist,name="mssglist"),
    path("userlist",views.userlist,name="userlist"),
    path('fapprove<int:id>',views.fapprove,name='fapprove'),
    path('freject<int:id>',views.freject,name='freject'), 
]