from .views import User
from django.contrib import admin
from .models import UserModel, StudentModel

# Register your models here.
@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('matric_number','level','school')
    
@admin.register(UserModel,)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('username','first_name', 'email')


