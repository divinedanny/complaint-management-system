from django.db import models
from student.models import UserModel
# Create your models here.


class StaffModel(models.Model):
    
    department_choice = (
        ('admin','administration'),
        ('busary','busary'),
        ('security','security'),
        ('hall','hall Adminstration'),
        ('busa','student Administration'),
        ('bumu','student Community Grade'),
        ('registry','registry'),
        ('cafeteria','Cafeteria')

    )
    
    
    staff = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    staff_number = models.CharField(max_length=10, unique=True, blank=False)
    department = models.CharField(choices=department_choice, max_length=25)
    
