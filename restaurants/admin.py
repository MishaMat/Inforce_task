from django.contrib import admin
from .models import *


@admin.register(RestaurantModel)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rating', 'address', 'contact_no']


@admin.register(MenuModel)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['restaurant', 'date', 'vote']


@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(VoteModel)
class VoteAdmin(admin.ModelAdmin):
    pass
