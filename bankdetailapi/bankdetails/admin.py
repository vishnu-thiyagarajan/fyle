from django.contrib import admin
from .models import BankDetails
from import_export.admin import ImportExportModelAdmin
# Register your models here.


# admin.site.register(BankDetails)
@admin.register(BankDetails)
class BankDetailsAdmin(ImportExportModelAdmin):
    pass
