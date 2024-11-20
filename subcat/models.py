from django.db import models
from home.models import Category
# Create your models here.
class Subcat(models.Model):
    type=models.CharField(max_length=120)
    cat=models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.type
    
    class Meta:
        db_table='sub_category'

        