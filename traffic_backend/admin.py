from django.contrib import admin
from .models import flows, category, coordinates
# Register your models here.
admin.site.register(flows)
admin.site.register(category)
admin.site.register(coordinates)