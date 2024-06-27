from django.contrib import admin
from .models import Customer, Order
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class CustomerAdmin(UserAdmin):
    model = Customer
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('customer_code','name', 'phone_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('customer_code', 'name','phone_number')}),
    )

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order)