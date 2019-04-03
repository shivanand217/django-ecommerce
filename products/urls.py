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
    url(r'^featured/$', ProductFeaturedListView.as_view(), name='featured'),
    url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view(), name='featured-details'),
    url(r'^products/$', ProductListView.as_view(), name='list'),
    url(r'^products-fbv/$', product_list_view, name='fbv-list'),
    url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='detail'),
    url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
    url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view, 'fbv-detail'),
]