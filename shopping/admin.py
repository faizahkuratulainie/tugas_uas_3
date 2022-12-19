from django.contrib import admin
from shopping.models import Shop
# Register your models here.

class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'diskripsi', 'harga']
    search_fields = ['name', 'diskripsi', 'harga']
    list_filter = ('harga',)
    list_per_page = 4

admin.site.register(Shop, ShopAdmin)