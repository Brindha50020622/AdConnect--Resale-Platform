from django.urls import path
from . import views
urlpatterns=[
   
    path('postad',views.postad,name='postad'),
    path('postad/<str:email>/', views.postad, name='postad'),
    path('single',views.single,name='single'),
    path('myposts',views.myposts,name='myposts'),
    path('delete',views.delete,name='delete')
]