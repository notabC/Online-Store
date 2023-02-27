from rest_framework import serializers

from .models import *


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        # fields = ['item_no','item_description','item_price','number_of_items']
