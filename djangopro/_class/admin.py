from django.contrib import admin

from djangopro._class.models import Class


# Register your models here.
# admin.TabularInLine or admin.StackedInline
class EnrollmentInLine(admin.StackedInline):
    model = Class.students.through
    extra = 1
    readonly_fields = ('date',)
    autocomplete_fields = ('user',)
    ordering = ('-date',)


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    inlines = [EnrollmentInLine]
    list_display = ('name', 'slug', 'begin', 'end',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-begin',)
