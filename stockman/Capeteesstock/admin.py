from django.contrib import admin
from .models import Product,NewItem
from .forms import NewItemForm
# Register your models here.
admin.site.register(Product)
admin.site.register(NewItem)
