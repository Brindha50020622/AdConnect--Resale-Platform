from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from register.models import Location
from home.models import Category
from .models import Subcat
from products.models import Product
def subcat(request):
        loc=Location.objects.all()
        cat=Category.objects.all()
        stype = request.GET.get('type')
        email=request.GET.get('email')
        print(stype)
        sub=Subcat.objects.get(type=stype)
        subcat=sub.id      
        products= Product.objects.filter(subcat_id=subcat)              
        return render(request,'mobiles.html',{'location':loc,'category':cat,'product':products,'email':email})