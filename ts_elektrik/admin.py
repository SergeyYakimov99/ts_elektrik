from django.contrib import admin

from .models import Factory, Retail_network, Sole_trader, Contacts, Products


class FactoryAdmin(admin.ModelAdmin):
    list_display = ("title", "contacts", "products", "created")
#    search_fields = ("contacts__city")
    list_filter = ('contacts__city',)


class Retail_networkAdmin(admin.ModelAdmin):
    list_display = ("title", "contacts", "products", "created", "debt")
    search_fields = ("contacts__city",)


class Sole_traderAdmin(admin.ModelAdmin):
    list_display = ("title", "contacts", "products", "created", "debt")
    search_fields = ("title", "city")
    list_filter = ("contacts__city",)


class ContactsAdmin(admin.ModelAdmin):
    list_display = ("email", "land", "city", "street", "house")
    search_fields = ("email", "land", "city", "street", "house")


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("title", "brand", "release_date")


admin.site.register(Factory)
admin.site.register(Retail_network)
admin.site.register(Sole_trader)
admin.site.register(Contacts)
admin.site.register(Products)
