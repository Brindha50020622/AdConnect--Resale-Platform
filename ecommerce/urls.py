
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/',include('register.urls')),
    path('',include('register.urls')),
    path('admin/', admin.site.urls),
    path('home/',include('home.urls')),
    path('subcat/',include('subcat.urls')),
    path('postad/',include('products.urls')),
    path('single/',include('products.urls')),
    path('myposts/',include('products.urls')),
    path('delete/',include('products.urls')),
    path('customadmin/',include('customadmin.urls'))
    
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)