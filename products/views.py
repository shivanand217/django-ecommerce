from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from products.models import *

# Create your views here.
# Add the views created here to your urls.py

# Class based views
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    # to get context in class based views
    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print(context)        
        return context

# function based views
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)

# Class based views
class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
 
# function based views
def product_detail_view(request, pk=None, *args, **kwargs):
    instance = get_object_or_404(Product, pk=pk)
    print(instance)
    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)
    