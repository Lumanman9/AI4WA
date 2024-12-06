from django.contrib import admin
from .models import Crime


# Register your models here.

@admin.register(Crime)
class CrimeAdmin(admin.ModelAdmin):
    list_display = ('name','count','created_at','updated_at')
    search_fields = ('name','count')
    list_filter = ('created_at','updated_at')
    fieldsets = (
        (
            'Crime Information',
            {
                'fields': (
                    'name',
                    'description',
                    'count',
                )
            },
        ),
    )