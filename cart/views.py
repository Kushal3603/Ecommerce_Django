from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
from django.contrib import messages

def cart_summary(request):
    cart=Cart(request)
    cart_products=cart.get_prods()
    quantities=cart.get_quants()
    totals=cart.cart_total()
    return render(request,'cart_summary.html',{"cart_products":cart_products,"quantities":quantities,"totals":totals})

def cart_add(request):
    cart=Cart(request)
    if request.POST.get('action')=='post':
        product_id=int(request.POST.get('product_id'))
        product_qty=int(request.POST.get('product_qty'))
        product=get_object_or_404(Product, id=product_id)
        cart.add(product=product,quantity=product_qty)
        cart_quantity=cart.__len__()
        response=JsonResponse({'qty':cart_quantity})
        messages.success(request,("Product Added to Cart."))
        return response
        # response=JsonResponse({'Product Name: ':product.name})
        # return response

def cart_update(request):
    if request.method == 'POST' and request.POST.get('action') == 'post':
        # Fetch product ID and quantity from POST data
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        # Update the cart using the Cart class
        cart = Cart(request)
        cart.update(product_id=product_id, quantity=product_qty)

        # Get the updated cart quantity
        cart_quantity = cart.__len__()
        # Return the updated cart quantity as a JSON response
        response= JsonResponse({'qty': cart_quantity})
        messages.success(request,("Your Cart Has Been Updated."))
        return response

    return JsonResponse({'error': 'Invalid request'}, status=400)

def cart_delete(request):
    cart=Cart(request)
    if request.POST.get('action')=='post':
        product_id=int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        response=JsonResponse({'product':product_id})
        messages.success(request,("Item Has Been Deleted From The Cart."))
        return response
