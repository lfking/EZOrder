import os
from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_GET, require_POST
from ezorder import tasks

@require_GET
def get_index(request):
    return render_to_response('index.html',
                              {
        'selected_nav': 'index',
    })

@require_GET
def shopping_list(request):
    return render_to_response('shopping_list.html',
                              {
        'selected_nav': 'shop',
    })

#@require_POST
def order(request):
    channel = os.urandom(16).encode('hex')
    t = tasks.track_order(channel)
    return render(request, 'order.html', {'channel': channel})
