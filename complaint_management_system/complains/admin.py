from django.contrib import admin
from .models import ComplainsModel
# Register your models here.

@admin.register(ComplainsModel)
class ComplainsAdmin(admin.ModelAdmin):
    list_display = ('owner', 'complain_status', 'department')