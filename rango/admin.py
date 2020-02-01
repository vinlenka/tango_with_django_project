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


admin.site.register(Category)
admin.site.register(Page, PageAdmin)
