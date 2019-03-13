from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from products.models import Product

# Create your views here.
# Add the views created here to your urls.py

# Class based views
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(ProductListView, self).dispatch(request, *args, **kwargs)

    # to get context in class based views
    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        print(context)        
        return context

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    # @method_decorator(login_required)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(ProductDetailView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

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
    # Various queryset examples

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
    print(qs)
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