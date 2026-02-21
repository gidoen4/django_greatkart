from django.shortcuts import render
from django.http import HttpResponse

from carts.models import CartItem

# Create your views here.
def place_order(request):
    current_user = request.user

    # if the carts count is less than or equal to 0 , thhen redirect them to store
    cart_items = CartItem.objects.filter(user=current_user)