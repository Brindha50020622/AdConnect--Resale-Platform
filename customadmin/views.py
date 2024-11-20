from django.shortcuts import render
from register.models import User
from products.models import Product,SubcatCount
from subcat.models import Subcat
from home.models import Category

# Create your views here.
def customadmin(request):
    user_count = User.objects.count()
    tproduct_count = Product.objects.count()
    subcategories = Subcat.objects.all()
    subcategory_types = [subcat.type for subcat in subcategories]  
    categories = Category.objects.all()
    subs=[]
    for category in subcategories:
        sub = SubcatCount.objects.get(subcat_id=category.id)
        subs.append((category.type, sub.count))
    cat = []
    for category in categories:
        s= Subcat.objects.filter(cat=category)
        count=0
        for i in s:
            sub = SubcatCount.objects.get(subcat_id=i.id)
            count+=sub.count
        cat.append((category.name,count))
    
    return render(request,"admin.html",{'user_count':user_count,'product_count':tproduct_count,'stype':subcategory_types,'subs':subs,'cat':cat})