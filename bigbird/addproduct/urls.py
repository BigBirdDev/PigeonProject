from django.urls import path
from .views import add_product_view

app_name = 'addproduct'

urlpatterns = [
    path('add-product/', add_product_view, name='add_product'),
    # Add other URL patterns as needed
]
