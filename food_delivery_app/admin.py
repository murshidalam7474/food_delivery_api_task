from django.contrib import admin
from .models import Item, Organization, Pricing

admin.site.register(Item)
admin.site.register(Organization)
admin.site.register(Pricing)
