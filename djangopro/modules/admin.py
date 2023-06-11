from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from djangopro.modules.models import Module


# Register your models here.
@admin.register(Module)
class ModuleAdmin(OrderedModelAdmin):
    list_display = ('title', 'public', 'move_up_down_links')
