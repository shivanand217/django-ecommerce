import random
import os
from django.db import models
from products.utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

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

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True)

class ProductManager(models.Manager):    
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self): # for calling Product.objects.featured()
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True) # slug field for better readability
    description = models.TextField(max_length=400) 
    price = models.DecimalField(decimal_places=2,max_digits=15,default=10.99)
    image = models.ImageField(null=True, blank=True, upload_to='products/')
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_digital = models.BooleanField(default=False)

    objects = ProductManager()

    def get_absolute_url(self):
        #return "/products/{slug}/".format(slug=self.slug)
        return reverse("products:detail", kwargs={"slug": self.slug})
    
    # __str__ function helps in defining the representation of the model
    # or it tells what that object is. 
    def __str__(self): # for python3
        return self.title

    def __unicode__(self): # for python2
        return self.title

def product_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    
pre_save.connect(product_pre_save_reciever, sender=Product)