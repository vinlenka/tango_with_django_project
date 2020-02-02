from django.contrib import admin
from rango.models import Category, Page


# Register your models here.

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title']}),
        ('Category', {'fields': ['category']}),
        ('URL', {'fields': ['url']})
    ]
    list_display = ('title', 'category', 'url')
    # inlines = [ChoiceInline]

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

