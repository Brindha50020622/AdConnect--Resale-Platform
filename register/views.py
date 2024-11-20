from django.shortcuts import render, redirect
from .models import User,Location

def register(request):
    if request.method == 'POST':
        
        uname=request.POST['name']
        uemail=request.POST['email']
        ucontact=request.POST['contact']
        ulocation=request.POST['location']
        upwd=request.POST['password']
        pwd1=request.POST['password1']
        
        if upwd==pwd1:
         if User.objects.filter(uemail=uemail).exists():
                
                error_message = "User with this email already exists."
                return render(request, 'register.html', {'error_message': error_message})
         try: 
            location = Location.objects.get(location=ulocation) 
         
         except Location.DoesNotExist:
            error_message = "Ensure that your location is within Chennai, Coimbatore, Bengaluru, Kolkata, Ahmedabad, Hyderabad, Pune, Mumbai, Jaipur, Lucknow, Kochi, Visakhapatnam, or Delhi." 
            return render(request, 'register.html', {'error_message': error_message})
        
         user=User.objects.create(uname=uname,uemail=uemail,ucontact=ucontact,ulocation=location,upwd=upwd)
         user.save()         
         return render(request,'index.html',{})
        else:   
             error_message = "Password doesnt match"
             return render(request, 'register.html', {'error_message': error_message})
  
    return render(request,'register.html',{})

def login(request):
    if request.method == 'POST':        
        uemail=request.POST['email']
        upwd=request.POST['pwd']
        if uemail and upwd:
            try:
                user = User.objects.get(uemail=uemail)
            except User.DoesNotExist:
                error_message='User with this email address does not exist.'
                return render(request, 'login.html', {'error_message': error_message})
            else:
                if user.upwd !=upwd:
                   error_message= 'Incorrect password.'
                   return render(request, 'login.html', {'error_message': error_message})
                elif user.superuser:
                    return redirect('customadmin')
            return render(request,'index.html',{'email':uemail})
    return render(request,'login.html',{})

        

