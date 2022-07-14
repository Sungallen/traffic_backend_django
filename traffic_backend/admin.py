from django.contrib import admin
from .models import flows, category, coordinates
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class FlowsAdmin(ImportExportModelAdmin):
    pass
#admin.site.register(flows, FlowsAdmin)
admin.site.register(category, FlowsAdmin)

@admin.register(coordinates)
class coordinatesAdmin(FlowsAdmin):
    list_display = ("descriptions", "coordinates")

@admin.register(flows)
class flowsAdmin(ImportExportModelAdmin):
    list_display = ("category", "flow", "coordinates", "time")
    search_fields = ["category__category", "time"]
