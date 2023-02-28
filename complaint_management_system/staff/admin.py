from django.contrib import admin
from .models import StaffModel

# Register your models here.
@admin.register(StaffModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('staff_number', 'department')
    
