from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Restaurant(models.Model):
    """Model that represents restaraunt"""

    title = models.CharField(unique=True, max_length=100)
    address = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = _('restaurant')
        verbose_name_plural = _('restaurants')

    def __str__(self):
        return str(self.title)

class MenuItem(models.Model):
    """Model that represents menu item"""

    title = models.CharField(max_length=100)
    cost = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(0)])
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menuitems')

    class Meta:
        verbose_name = _('menu item')
        verbose_name_plural = _('menu items')

    def __str__(self):
        return str(self.title)
    

class Modifier(models.Model):
    """Model that represents modifier"""

    title = models.CharField(max_length=100)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.DO_NOTHING, related_name='modifiers')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='child')

    class Meta:
        verbose_name = _('modifier')
        verbose_name_plural = _('modifiers')

    def __str__(self):
        return str(self.title)
