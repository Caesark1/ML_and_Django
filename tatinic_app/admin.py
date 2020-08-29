from django.contrib import admin
from .models import Passenger
from import_export import resources
from import_export.admin import ImportExportMixin


class PassengerResource(resources.ModelResource):
    class Meta:
        model = Passenger



@admin.register(Passenger)
class PassengerAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ("Name", "Age", "Sex")

