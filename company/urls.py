from django.urls import path
from . import views
urlpatterns = [
    path('creg',views.creg,name="creg"),
    path('clog',views.clog,name="clog"),
    path('chome',views.chome,name="chome"),
    path('smssg',views.smssg,name="smssg"),
    path('vmssg<str:pk>',views.vmssg,name="vmssg"),
    path('mssgup/<int:id>',views.mssgup, name='mssgup'),
    path('mssgdlt/<int:pid>',views.mssgdlt, name='mssgdlt'),
    path('cprofile',views.cprofile, name='cprofile'),
    path('ceditpro/<int:id>',views.ceditpro, name='ceditpro'),
    path('notifi',views.notifi, name='notifi'),


]