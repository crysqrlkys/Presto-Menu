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
    children = serializers.SerializerMethodField(
        method_name='get_children_items')

    class Meta:
        model = Modifier
        fields = ('id', 'title', 'parent', 'children')
        read_only_fields = ('id', 'title', 'parent', 'children')

    def get_children_items(self, parent):
        serialized_data = ModifierSerializer(
            parent.child.all(), many=True, read_only=True, context=self.context)
        return serialized_data.data


class MenuItemSerializer(serializers.ModelSerializer):
    modifiers = serializers.SerializerMethodField(
        method_name='get_modifiers_items')

    class Meta:
        model = MenuItem
        fields = ('id', 'title', 'cost', 'modifiers')
        read_only_fields = ('id', 'title', 'cost', 'modifiers')

    def get_modifiers_items(self, item):
        modifiers = Modifier.objects.filter(
            menu_item=item, parent__isnull=True)
        serialized_data = ModifierSerializer(
            modifiers, many=True, read_only=True, context=self.context)
        return serialized_data.data