from django.contrib import admin

# Register your models here.
from src.models import CustomerInformations, PassportInformations

admin.site.register(CustomerInformations)
admin.site.register(PassportInformations)