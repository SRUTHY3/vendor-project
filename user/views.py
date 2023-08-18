from django.shortcuts import render, redirect
from .models import * 
from company.models import * 
from django.contrib import messages

def ureg(request):
    if request.method == "POST":
        name = request.POST['name'] 
        email = request.POST['email']
        place=request.POST['place']
        address=request.POST['address']  
        contact=request.POST['contact']
        password1 = request.POST['password']
        password2 = request.POST['RPassword']

        if password1 == password2:
            if   user_tb.objects.filter(email=email).exists():
                 messages.info(request, "email already exists")
            elif user_tb.objects.filter(contact=contact).exists():
                 messages.info(request, "contact already exists")
            
            
            else:
                caters = user_tb(name=name,contact=contact, 
                password=password1,email=email,place=place,address=address)
                caters.save()            
                return redirect('ulog')
    return render(request, 'user/ureg.html')

def ulog(request):
    if request.method=="POST":
        try:
            email = request.POST['email']
            password = request.POST['password']
            login=user_tb.objects.get(email=email,password=password)
            request.session['email']=login.email
            request.session['id']=login.id
            return redirect('uhome')
        except user_tb.DoesNotExist as o:
            messages.info(request, "Invalid login credentials")
    return render(request, 'user/ulog.html')

def uhome(request):
    showspace=company_tb.objects.all()
    if request.method=="POST":
        Location=request.POST.get('Location').upper()
        srch=company_tb.objects.filter(dist=Location)
        return render(request,'user/searching.html', {'pro':srch,'Location':Location})
    return render(request,'user/uhome.html',{'pro':showspace})

# def search(request):
#     if request.method == "POST":
#         query_name = request.POST.get('city', None)
#         if query_name:
#             results = Hotel_reg.objects.filter(city=query_name)
#             return render(request, 'user/hresult.html', {"results":results})
#         else:
#             messages.info(request,"Not Found")

#     return render(request, 'user/hresult.html')



def searching(request):
    return render(request,'user/searching.html')

# def citysearch(request,cid):
#     ss=company_tb.objects.get(id=cid)
#     if request.method=="POST":
#         City=request.POST.get('city').upper()
#         cm=company_tb.objects.filter(city=City)
#         return render(request,'user/city.html', {'cm':cm})
#     return render(request,'user/citysearch.html',{'cm':ss})




def citysearch(request,cid):
    # ss=company_tb.objects.filter(dist=cid)
    district=cid
    if request.method=="POST":
        City=request.POST.get('city').upper()
        cm=company_tb.objects.filter(city=City,dist=district)
        return render(request,'user/city.html', {'cm':cm})
    return render(request,'user/citysearch.html')

def city(request):
    return render(request,'user/city.html')


def discomdetail(request,id):
    ss=company_tb.objects.get(id=id)
    return render(request,'user/discomdetail.html',{'cm':ss})
def citcomdetail(request,pid):
    ss=company_tb.objects.get(id=pid)
    return render(request,'user/citcomdetail.html',{'cm':ss})

def uprofile(request):
    hid=request.session['id']
    prof=user_tb.objects.get(id=hid)
    return render(request,'user/uprofile.html', {'pro':prof})

def ueditpro(request,id):
    edit=user_tb.objects.get(id=id)
    if request.method=="POST":
        edit.name = request.POST['name'] 
        edit.email = request.POST['email']
        edit.place=request.POST['place']
        edit.address=request.POST['address']
        edit.contact=request.POST['contact']
        edit.password = request.POST['password']
        edit.save()
        return redirect("uprofile")
    return render(request,'user/ueditpro.html',{'pro':edit})
