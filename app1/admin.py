from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Product)
class Custom_admin_shop(admin.ModelAdmin):
    list_display = ['name', 'price', 'islike', 'image_tag',]
    list_filter = ['name', 'price', 'islike' ]
    
    readonly_fields = ('image_tag',)