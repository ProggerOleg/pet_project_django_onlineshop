from django.contrib import admin
from .models import *
# Register your models here.


class ShopListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'available')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('available',)
    list_filter = ('available', 'time_create')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(ShopList, ShopListAdmin)
admin.site.register(Category, CategoryAdmin)
