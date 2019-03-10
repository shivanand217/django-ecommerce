import random
import os
from django.db import models

# Create your models here.

def get_filename_extension(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(filename)
    print("name and extension are", name, ext)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,400000) # random integer
    name, ext = get_filename_extension(filename)
    final_filename = '{new_filename}{ext}'.format(
        new_filename=new_filename,
        ext=ext
    )
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField() 
    price = models.DecimalField(decimal_places=2,max_digits=15,default=10.99)
    image = models.FileField(null=True, blank=True, upload_to='products/')
    
    # __str__ function helps in defining the representation of the model
    # or it tells what that object is. 
    def __str__(self): # for python3
        return self.title

    def __unicode__(self): # for python2
        return self.title