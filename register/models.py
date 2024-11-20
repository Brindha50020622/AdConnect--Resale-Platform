from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
# Create your models here.
def validate_email(value):
    if User.objects.filter(uemail=value).exists():
        raise ValidationError("Email already exists.")
    
class Location(models.Model):
    location=models.CharField(max_length=25,default='N/A')
    latitude=models.DecimalField(max_digits=10,decimal_places=4)
    longtitude=models.DecimalField(max_digits=10,decimal_places=4)
    class Meta:
        db_table="Location"
    
class User(models.Model):
    
    uname=models.CharField(max_length=120)
    uemail=models.EmailField(validators=[EmailValidator(),validate_email])
    ucontact=models.CharField(max_length=15)
    ulocation=models.ForeignKey(Location, on_delete=models.CASCADE)
    upwd=models.CharField(max_length=10)
    superuser = models.BooleanField(default=False)

    class Meta:
        db_table="user"
       
  