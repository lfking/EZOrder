import os
import json
import tempfile
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt
from ezorder import tasks
import parse_ingredients
from ocr import ocr_image

import braintree

braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id="9rqw2d8p69gj79hc",
                                  public_key="zxvcz8gyj7t4rz99",
                                  private_key="bb48c79b6a076781ff6aa6c1afad45f0")

@require_GET
def get_index(request):
    return render_to_response('index.html',
                              {
        'selected_nav': 'index',
    })

@require_POST
@csrf_exempt
def ocr(request):
    assert 'webcam' in request.FILES
    fd, path = tempfile.mkstemp('.jpg')
    f = os.fdopen(fd, 'wb')
    try:
        for chunk in request.FILES['webcam'].chunks():
            f.write(chunk)
        f.close()
        recipe_text = ocr_image(path)
    finally:
        os.remove(path)
    items = parse_ingredients.parse(recipe_text)
    return JsonResponse(items)

@require_GET
def shopping_list(request):
    items = [
  {
    'selected': True,
    'brands': [
         {'name': '1L Olivia olive oil', 'quantity': 2, 'weight_unit': None, 'price': 1000},
         {'name': '2L Tnuva olive oil', 'quantity': 1, 'weight_unit': None,'price': 1200},
    ],
  },
  {
    'selected': True,
    'brands': [
         {'name': 'Tomatos', 'quantity': 2, 'unit_weight': 0.5, 'weight_unit': 'kg', 'price': 500},
         {'name': 'Organic Tomatos', 'quantity': 5, 'unit_weight': 0.2, 'weight_unit': 'kg', 'price': 200}
    ],
  },
  {
    'selected': False,
    'brands': [
         {'name': '500g Kosher Salt', 'quantity': 1, 'weight_unit': None, 'price': 6200},
         {'name': '2L Tnuva olive oil', 'quantity': 1, 'weight_unit': None, 'price': 5800}
    ],
  }
]
    data = json.dumps(items)
    return render_to_response('shopping_list.html',
                              {
        'selected_nav': 'shop',
        'items': data,
    })

@require_GET
def order(request):
    channel = os.urandom(16).encode('hex')
    t = tasks.track_order(channel)
    return render(request, 'order.html', {'channel': channel})


#@require_POST
def pay(request):
    return render(request, 'pay.html')

@require_POST
def create_purchase(request):
    nonce = request.POST["payment_method_nonce"].encode('utf8')
    result = braintree.Transaction.sale({
        "amount": "10.00",
        "payment_method_nonce": nonce
    })
    assert result.is_success
    return redirect('order')

@require_GET
def client_token(request):
    print 'hey'
    return HttpResponse(braintree.ClientToken.generate())
