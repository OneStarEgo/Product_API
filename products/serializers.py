from itertools import product
from rest_framework import serializers
from .models import

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ['id', 'title', 'description', 'price', 'inventory_quantity' ]