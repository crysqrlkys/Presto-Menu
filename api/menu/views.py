from django.db.models import Prefetch
from django.http import Http404 
from rest_framework import viewsets
from .models import MenuItem, Modifier, Restaurant
from .serializers import MenuItemSerializer, RestaurantSerializer


class RestaurantView(viewsets.ReadOnlyModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class MenuItemView(viewsets.ReadOnlyModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_queryset(self, *args, **kwargs):
        children = Prefetch('modifiers', queryset=Modifier.objects.filter(parent_id__isnull=True).select_related('parent'))
        qs = super().get_queryset().filter(restaurant=self.kwargs.get('restaurant_pk')).prefetch_related(children)
        if not qs:
            raise Http404()
        return qs
