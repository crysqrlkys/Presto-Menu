from django.contrib import admin
from .models import (
    Restaurant,
    MenuItem,
    Modifier
)

admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Modifier)