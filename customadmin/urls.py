from django.urls import path
from . import views
urlpatterns=[
    
    path('customadmin',views.customadmin,name='customadmin'),
    
]