from django.conf.urls import url

from products.views import (
    ProductDetailView,
    ProductListView,
    product_detail_view,
    product_list_view,
    ProductFeaturedListView,
    ProductFeaturedDetailView,
    ProductDetailSlugView
    )

urlpatterns = [
    url(r'^featured/$', ProductFeaturedListView.as_view()),
    url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
    url(r'^products/$', ProductListView.as_view()),
    url(r'^products-fbv/$', product_list_view),
    url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
]