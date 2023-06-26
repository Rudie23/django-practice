from django.contrib import admin

from djangopro._class.models import Class


# Register your models here.

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'begin', 'end',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-begin',)
