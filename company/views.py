from django.contrib import messages
from django.shortcuts import render, redirect
from .models import * 
# Create your views here.
def creg(request):
    if request.method == "POST":
        name = request.POST['name'] 
        bname = request.POST['bname'] 
        email = request.POST['email']
        place=request.POST['place']
        address=request.POST['address']
        city=request.POST['city']
        dist=request.POST['dist']
        contact=request.POST['contact']
        state=request.POST['state']
        bimg=request.FILES['bimg']
        password1 = request.POST['password']
        password2 = request.POST['RPassword']

        if password1 == password2:
            if   company_tb.objects.filter(email=email).exists():
                 messages.info(request, "email already exists")
            elif company_tb.objects.filter(contact=contact).exists():
                 messages.info(request, "contact already exists")
            elif company_tb.objects.filter(bname=bname).exists():
                 messages.info(request, "bname already exists")
            
            else:
                caters = company_tb(name=name,bname=bname,contact=contact, 
                password=password1,email=email,place=place,address=address,city=city.upper(),state=state,bimg=bimg,dist=dist.upper())
                caters.save()            
                return redirect('clog')
    return render(request, 'company/creg.html')


def clog(request):
    if request.method=="POST":
        try:
            bname = request.POST['bname']
            password = request.POST['password']
            login=company_tb.objects.get(bname=bname,password=password)
            request.session['bname']=login.bname
            request.session['id']=login.id
            return redirect('chome')
        except company_tb.DoesNotExist as o:
            messages.info(request, "Invalid login credentials")
    return render(request, 'company/clog.html')

def chome(request):
    return render(request,'company/chome.html')

def smssg(request):
    if request.method=="POST":
            mssg = request.POST['msg'] 
            cid = request.POST['cid'] 
            mss=Com_mssg(mssg=mssg,Companyid_id=cid)
            mss.save()
            return redirect('chome')
    return render(request,'company/smssg.html')

def vmssg(request,id):
    vm=company_tb.objects.get(id=request.session['id'])
    return render(request,'company/vmssg.html')

def vmssg(request,pk):
    mg=Com_mssg.objects.filter(Companyid=pk)
    return render(request,'company/vmssg.html',{'mg':mg})

def mssgup(request,id):
    prod=Com_mssg.objects.get(id=id)
    if request.method=="POST":       
        prod.mssg=request.POST.get("msg")
        prod.save()
        return redirect("chome")
    return render(request,'company/mssgup.html',{'prod':prod})
    

def mssgdlt(request,pid):
    prod = Com_mssg.objects.get(id=pid)
    if request.method == "POST":
        prod.delete()
        return redirect("chome")
    return render(request,'company/mssgdlt.html',{'prod':prod})


def cprofile(request):
    hid=request.session['id']
    prof=company_tb.objects.get(id=hid)
    return render(request,'company/cprofile.html', {'pro':prof})

def ceditpro(request,id):
    edit=company_tb.objects.get(id=id)
    if request.method=="POST":
        
        if len(request.FILES)!=0:
   
            edit.bimg=request.FILES.get('bimg')

        edit.name = request.POST['name'] 
        edit.bname = request.POST['bname'] 
        edit.email = request.POST['email']
        edit.place=request.POST['place']
        edit.address=request.POST['address']
        edit.city=request.POST['city']
        edit.dist=request.POST['dist']
        edit.contact=request.POST['contact']
        edit.state=request.POST['state']
        edit.password = request.POST['password']
        edit.save()
        return redirect("cprofile")
    return render(request,'company/ceditpro.html',{'pro':edit})

def notifi(request):
    nt=Com_mssg.objects.all()
    return render(request,'company/notifi.html',{'nt':nt})