import os
import json
import tempfile
from django.http import HttpResponse, JsonResponse
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
    return JsonResponse({'data': items})

#@require_POST
@csrf_exempt
def shopping_list(request):
    print request.POST
    data = request.POST['data']
    #data = ('[{"products":[{"price":1500,"unit_weight":null,"name":"chicken stock power","weight_unit":null,"quantity":1}],"starts_disabled":false}]')
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


@require_POST
@csrf_exempt
def pay(request):
    data = json.loads(request.POST['data'])
    cents = parse_ingredients.get_price(data)
    return render(request, 'pay.html', {'price': "%s.%s" % (cents / 100, cents % 100) })

@require_POST
def create_purchase(request):
    nonce = request.POST["payment_method_nonce"].encode('utf8')
    price = request.POST["amount"].encode('utf8')
    result = braintree.Transaction.sale({
        "amount": price,
        "payment_method_nonce": nonce
    })
    assert result.is_success
    return redirect('order')

@require_GET
def client_token(request):
    print 'hey'
    return HttpResponse(braintree.ClientToken.generate())
