from django.shortcuts import redirect, render
from django.http import HttpResponse

from carts.models import CartItem
from orders.forms import OrderForm

# Create your views here.
def place_order(request):
    current_user = request.user

    # if the carts count is less than or equal to 0 , thhen redirect them to store
    cart_items = CartItem.objects.filter(user=current_user)
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('store')
    
    if request.method == 'POST':
        form = OrderForm(request.POST)