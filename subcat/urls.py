from django.urls import path
from . import views
urlpatterns=[   
    path('subcat',views.subcat,name='subcat')
]