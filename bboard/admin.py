from django.contrib import admin

from .models import BBoard as bb
from .models import Category as cat
# Register your models here.

class BbAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'content', 'price', 'category', 'date')
    list_display_links = ('user', 'title')
    search_fields = ('title', 'price')


admin.site.register(bb, BbAdmin)
admin.site.register(cat)