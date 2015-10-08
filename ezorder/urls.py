from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^order/$', 'ezorder.views.order', name='order'),
    url(r'^shopping_list/$', 'ezorder.views.shopping_list', name='shopping-list'),
)
