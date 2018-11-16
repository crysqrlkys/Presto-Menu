from django.contrib import admin
from django.urls import path

from api.menu.urls import urlpatterns as api_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
] + api_urlpatterns
