from django.contrib import admin
from .models import UserModel

# Register your models here.
@admin.register(UserModel)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('username','matric_number','first_name','level')
