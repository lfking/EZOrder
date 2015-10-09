from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^order/$', 'ezorder.views.order', name='order'),
    url(r'^ocr/$', 'ezorder.views.ocr', name='ocr'),
    url(r'^shopping_list/$', 'ezorder.views.shopping_list', name='shopping-list'),
    url(r'^pay/$', 'ezorder.views.pay', name='pay'),
    url(r'^checkout/$', 'ezorder.views.create_purchase', name='checkout'),
    url(r'^client_token/$', 'ezorder.views.client_token', name='client_token')
)
