from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class item(models.Model):
    def __str__(self):
        return self.itemname  
    
    username=models.ForeignKey(User,on_delete=models.CASCADE, default=1)   
    itemname=models.CharField(max_length=200)
    itemprice=models.IntegerField()
    itemdesc=models.CharField(max_length=200)
    itemimage=models.CharField(max_length=1000, default='https://png.pngtree.com/element_our/20200702/ourmid/pngtree-vector-illustration-knife-and-fork-western-food-plate-image_2283844.jpg')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'itemid':self.pk})
        # return reverse('detail', args=[str(self.pk)])