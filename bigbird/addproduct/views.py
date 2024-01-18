from django.shortcuts import render

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def add_product_view(request):
    # Your view logic for the authenticated user
    return render(request, 'addproduct/add_product.html')