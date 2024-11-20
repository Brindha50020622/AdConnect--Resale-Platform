from django.shortcuts import render
from subcat.models import Subcat
from .models import Product
from register.models import User
import math
from register.models import Location
# Create your views here.
def postad(request):
    sub=Subcat.objects.all()
    email=request.GET.get('email')
    if request.method=="POST":
        oname = request.POST['oname']
        name = request.POST['name']
        description = request.POST['desc']
        cost = float(request.POST['cost'])
        offer = float(request.POST['offer'])
        brand = request.POST['brand']
        owner = User.objects.get(uname=oname) 
        sub = request.POST['subcat'] 
        sub = Subcat.objects.get(type=sub)     
        image = request.FILES['image']
        product = Product(name=name,image=image, description=description, cost=cost, offer=offer, brand=brand, ownerid_id=owner.id, subcat_id=sub.id)
        product.save()
        return render(request,'index.html',{'email':email})
    
    return render(request,'post-ad.html',{'subcat':sub,'email':email})

def distance(lat1,lon1,lat2,lon2):
        R = 6371
        lat1 = math.radians(lat1)
        lon1 = math.radians(lon1)
        lat2 = math.radians(lat2)
        lon2 = math.radians(lon2)          
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        dis=R*c
        return (dis)

def single(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    product=Product.objects.get(name=name)
    owner=User.objects.get(id=product.ownerid_id)
    user=User.objects.get(uemail=email)
    lo=Location.objects.get(id=owner.ulocation_id)    
    lu=Location.objects.get(id=user.ulocation_id)
    dis=distance(lo.latitude,lo.longtitude,lu.latitude,lu.longtitude)
    print(dis)
    
    return render(request,'single.html',{'products':product,'owner':owner,"distance":dis,"location":lo,"loc1":lu,'email':email})

def myposts(request):
     email=request.GET.get('email')
     user=User.objects.get(uemail=email)
     product=Product.objects.filter(ownerid_id=user.id)
     return render(request,'mypost.html',{'product':product,'email':email})

def delete(request):
     email=request.GET.get('email')
     if request.method=="POST":
          pid=int(request.POST['product_id'])
          product=Product.objects.get(id=pid)
          product.delete()
          return render(request,'index.html',{'email':email})
     user=User.objects.get(uemail=email)
     product=Product.objects.filter(ownerid_id=user.id)
     return render(request,'mypost.html',{'product':product,'email':email})
     