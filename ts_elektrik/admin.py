from django.contrib import admin

from .models import BaseModel


class BaseModelAdmin(admin.ModelAdmin):
    list_display = ("title", "contacts", "created", "debt")
    search_fields = ("contacts__city")


admin.site.register(BaseModel)
