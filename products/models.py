from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=15,default=10.99)
    
    # __str__ function helps in defining the representation of the model
    # or it tells what that object is. 
    def __str__(self): # for python3
        return self.title

    def __unicode__(self): # for python2
        return self.title