from django.shortcuts import get_list_or_404
from rest_framework import viewsets

from .models import MenuItem, Restaurant
from .serializers import MenuItemSerializer, RestaurantSerializer


class RestaurantView(viewsets.ReadOnlyModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuItemView(viewsets.ReadOnlyModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_queryset(self, *args, **kwargs):
        return get_list_or_404(MenuItem,restaurant_id=self.kwargs.get('restaurant_pk'))
