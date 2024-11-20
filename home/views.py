from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Category
from subcat.models import Subcat

def home(request):
    email = request.GET.get('name')
    print(email)
    print("A")
    if request.method == 'POST':       
            cat=request.POST.get('category')
            categories = Category.objects.all()
            subcats = Subcat.objects.all()    
            return render(request,'categories.html',{'categories':categories,'subcat':subcats,'cat':cat,'email':email})    
    else:
           
           return render(request,"index.html")
    
