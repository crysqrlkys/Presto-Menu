from rest_framework import serializers
from .models import (
    Restaurant,
    MenuItem,
    Modifier
)


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'title', 'address')
        read_only_fields = ('id', 'title', 'address')


class ModifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modifier
        fields = ('id', 'title', 'parent')
        read_only_fields = ('id', 'title', 'parent')



class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('id', 'title', 'cost')
        read_only_fields = ('id', 'title', 'cost')
