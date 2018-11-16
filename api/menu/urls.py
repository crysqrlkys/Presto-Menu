from django.conf.urls import include, url
from rest_framework_nested import routers
from .views import MenuItemView, RestaurantView

router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantView, base_name='restaurants')

menu_items_router = routers.NestedSimpleRouter(
    router, r'restaurants', lookup='restaurant')
menu_items_router.register(r'item', MenuItemView, base_name='menu-item')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(menu_items_router.urls))
]
