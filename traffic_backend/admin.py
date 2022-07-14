from django.contrib import admin
from .models import flows, category, coordinates
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class FlowsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(flows, FlowsAdmin)
admin.site.register(category)
admin.site.register(coordinates)
