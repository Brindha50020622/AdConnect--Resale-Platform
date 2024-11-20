from django.db import models
from register.models import User
from subcat.models import Subcat

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    offer = models.DecimalField(max_digits=7, decimal_places=2)
    brand = models.CharField(max_length=255)
    ownerid = models.ForeignKey(User, on_delete=models.CASCADE)
    subcat=models.ForeignKey(Subcat, on_delete=models.CASCADE,default=1)
    class Meta:
        db_table="products"

class SubcatCount(models.Model):
    subcat = models.ForeignKey(Subcat, on_delete=models.CASCADE,unique=True)
    count = models.IntegerField(default=0)

    class Meta:
        db_table = "subcat_counts"

