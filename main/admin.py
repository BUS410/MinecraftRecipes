from django.contrib import admin

from . import models

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
	list_display = ('name', 'item_category',)
	prepopulated_fields = {'slug': ('name',)}


class ItemCategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)
	prepopulated_fields = {'slug': ('name',)}


class RecipeAdmin(admin.ModelAdmin):
	list_display = ('result',)


admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.ItemCategory, ItemCategoryAdmin)
admin.site.register(models.Recipe, RecipeAdmin)
