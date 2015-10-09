import os
import json
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from ezorder import tasks

@require_GET
def get_index(request):
    return render_to_response('index.html',
                              {
        'selected_nav': 'index',
    })

@require_POST
@csrf_exempt
def ocr(request):
    return HttpResponse('response')

@require_GET
def shopping_list(request):
    items = [
  {
    'selected': True,
    'brands': [
         {'name': '1L Olivia olive oil', 'quantity': 2, 'weight_unit': None},
         {'name': '2L Tnuva olive oil', 'quantity': 1, 'weight_unit': None},
    ],
  },
  {
    'selected': True,
    'brands': [
         {'name': 'Tomatos', 'quantity': 2, 'unit_weight': 0.5, 'weight_unit': 'kg'},
         {'name': 'Organic Tomatos', 'quantity': 5, 'unit_weight': 0.2, 'weight_unit': 'kg'}
    ],
  },
  {
    'selected': False,
    'brands': [
         {'name': '500g Kosher Salt', 'quantity': 1, 'weight_unit': None},
         {'name': '2L Tnuva olive oil', 'quantity': 1, 'weight_unit': None}
    ],
  }
]
    data = json.dumps(items)
    return render_to_response('shopping_list.html',
                              {
        'selected_nav': 'shop',
        'items': data,
    })

#@require_POST
def order(request):
    channel = os.urandom(16).encode('hex')
    t = tasks.track_order(channel)
    return render(request, 'order.html', {'channel': channel})
