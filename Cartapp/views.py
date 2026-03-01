from django.shortcuts import redirect, render
from auth_app.middleware import auth
from django.contrib.contenttypes.models import ContentType
from .models import CartItem


@auth
def add_to_cart(request, model_name, product_id):

    content_type = ContentType.objects.get(model=model_name.lower())
    product = content_type.get_object_for_this_type(id=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        content_type=content_type,
        object_id=product_id
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_page');



@auth
def cart_page(request):
    cart_items = CartItem.objects.filter(user=request.user)

    total = 0
    for item in cart_items:
        total += item.subtotal()

    return render(request, 'Cart/cart.html', {
    'cart_items': cart_items,
    'total': total
})
# Create your views here.
