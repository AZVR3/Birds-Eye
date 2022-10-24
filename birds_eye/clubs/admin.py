from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Member)

@admin.register(models.Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'slogan', 'description')
    search_fields = ('member',)
    
    fieldsets = (
        (None, {
            'fields': ('name', 'slogan', 'description')
        }),
        ('Search', {
            'fields': ('member',)
        }),
    )