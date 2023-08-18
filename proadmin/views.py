# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
import os
from company.models import *

from user.models import *
# Create your views here.


def alogin(request):
    if request.method=="POST":
        try:
            email=request.POST.get('adminemail')
            Password=request.POST.get('adminpwd')
            alogin=projectadmin.objects.get(Email=email,Password=Password)
            request.session['email']=alogin.Email
            request.session['id']=alogin.id
            return redirect('ahome')
        except projectadmin.DoesNotExist as e:
            messages.info(request,'Incorrect Password or Username')
    return render(request,'projadmin/alogin.html')

def ahome(request):
     return render(request,'projadmin/ahome.html')



def companylist(request):
    cl=company_tb.objects.all()
    return render(request,'projadmin/companylist.html',{'cl':cl})


def mssglist(request):
    cs=Com_mssg.objects.all()
    return render(request,'projadmin/mssglist.html',{'cs':cs})


def userlist(request):
    cr=user_tb.objects.all()
    return render(request,'projadmin/userlist.html',{'cr':cr})

def fapprove(request,id):
    Com_mssg.objects.filter(id=id).update(approve=True)
    return redirect('mssglist')
    

def freject(request,id):
    Com_mssg.objects.filter(id=id).update(reject=True)
    return redirect('mssglist')
