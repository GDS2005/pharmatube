from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'manufacturer', 'dosage', 'price', 'quantity_in_stock', 'expiration_date', 'supplier_id', 'supplier_name', 'supplier_contact', 'date_received', 'height' ,'width', 'length']