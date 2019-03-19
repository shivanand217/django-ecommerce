from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from products.models import Product

from products import utils

# Add the views created here to the urls.py
# Class based views

# Featured Products
class ProductFeaturedListView(ListView):
    template_name = "products/list.html"
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        print("featured user authenticated is",request.user.is_authenticated())
        return Product.objects.featured() # get featured products list from Models Manager

class ProductFeaturedDetailView(DetailView):
    template_name = "products/featured-detail.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()

# All Products
class ProductListView(ListView):
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)        
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()

class ProductDetailView(DetailView):
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print("class based view context is",context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        print("object of id",pk,"is requested")
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist..")
        return instance

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            print("queryset has returned items",qs)
            instance = qs.first()
        except:
            raise Http404("Nothing Here :(")
        return instance

# function based views
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    if request.user.is_authenticated():
        return render(request, "products/list.html", context)
    else:
        return redirect('/login')
 
def product_detail_view(request, pk=None, *args, **kwargs):
    # Various queryset approaches
    
    #instance = get_object_or_404(Product, pk=pk)
    # try: 
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product doesn't exist..")
    # except:
    #     print("huh?")

    # pick the first instance in the returned queryset
    qs = Product.objects.filter(id=pk)
    if qs.exists() and qs.count() == 1:
        instance = qs.first()
    else:
        raise Http404("Product doesn't exists..")

    context = {
        'object': instance
    }
    if request.user.is_authenticated():
        return render(request, "products/detail.html", context)
    else:
        return redirect('/login')