from telnetlib import Telnet
from tkinter.tix import Tree
from django.db import models
from student.models import UserModel
import uuid
# Create your models here.
class ComplainsModel(models.Model):
        
    def upload(instance, filename):
        """
        This function is used to upload the image to the database
        """
        image = f"images/{filename}"
        return image
    
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


    COMPLAIN_STATES = (
        ('PENDING','PENDING'),
        ('INITIALIZED','INITIALIZED'),
        ('RESOLVED','RESOLVED'),
        ('CONFIRMED','CONFIRMED'),
        ('FAILED','FAILED'),
    )
    
    id = models.UUIDField(default=uuid.uuid4(),primary_key=True, unique=True, editable=False)
    department = models.CharField(max_length=30, choices=department_choice)
    complain_message = models.TextField(max_length=None)
    owner = models.ForeignKey(UserModel,on_delete=models.CASCADE, blank=True, null=True)
    complain_upload = models.FileField(upload_to=upload, null=True, blank=True)
    complain_status = models.CharField(choices=COMPLAIN_STATES, default='INITIALIZED', blank=False, null=False , max_length=20)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return self.department
    
    
    
    




# CREATE TABLE <table_name> (
#   id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
#   department VARCHAR(30),
#   complain TEXT,
#   owner_id UUID REFERENCES <user_table>(id),
#   complain_upload VARCHAR(255),
#   complain_state VARCHAR(20),
#   created_date TIMESTAMP DEFAULT NOW(),
#   updated_date TIMESTAMP DEFAULT NOW(),
# );