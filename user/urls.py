from django.urls import path
from . import views
urlpatterns = [
    path('ureg',views.ureg,name="ureg"),
    path('ulog',views.ulog,name="ulog"),
    path('uhome',views.uhome,name="uhome"),
    path('uprofile',views.uprofile, name='uprofile'),
    path('ueditpro/<int:id>',views.ueditpro, name='ueditpro'),
    path('searching',views.searching,name="searching"),
    path('citysearch<str:cid>',views.citysearch,name="citysearch"),
    path('city',views.city,name="city"),
    path('discomdetail/<int:id>',views.discomdetail, name='discomdetail'),
    path('citcomdetail/<int:pid>',views.citcomdetail, name='citcomdetail'),
    
    
    ]