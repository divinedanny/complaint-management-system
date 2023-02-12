from django.db import models
from datetime import date
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
# Create your models here.
username_validation = UnicodeUsernameValidator()
class UserModel(AbstractUser):
    
    def profilePicture(instance, filename):
        user = AbstractUser.username
        i = 0
        while i < 0:
            i +=1
            filename= i
        return f'profile_pictures/{user}/profile{filename}'
    
    undergraduate_level_choice = (
        ('100','100'),
        ('200','200'),
        ('300','300'),
        ('400','400'),
        ('500','500'),
        ('600','600'),
    )
    school_choice=(
         ('medicine','MEDICINE'),
         ('physiology','DEPARTMENT OF PHYSIOLOGY'),
         ('histology','DEPARTMENT OF HISTOLOGY'),
         ('community medicine','DEPARTMENT OF COMMUNITY MEDICINE'),
         ('nutrition and dietetics','DEPARTMENT OF NUTRITION AND DIETETICS'),
         ('anatomy','Department of Anatomy'),
         ('biochemistry','Department of Biochemistry'),
         ('chaemical pathology','The Department of Chemical Pathology'),
         ('haematoloy and immunology','DEPARTMENT OF HAEMATOLOGY AND IMMUNOLOGY'),
         ('micro biology','DEPARTMENT OF MEDICAL MICROBIOLOGY'),
         ('software engineering','DEPARTMENT OF SOFTWARE ENGINEERING'),
         ('computer science','DEPARTMENT OF COMPUTER SCIENCE'),
         ('information technology','DEPARTMENT OF INFORMATION TECHNOLOGY'),
         ('Relegious Studies','DEPARTMENT OF RELIGIOUS STUDIES'),
         ('Languages and Literary Studies','Department of Languages and Literary Studies'),
         ('History and International Studies','Department of History and International Studies'),
         ('Music and Creative Arts','Department of Music and Creative Arts'),
         ('Education','Department of Education'),
         ('JURISPRUDENCE AND PUBLIC LAW','DEPARTMENT OF JURISPRUDENCE AND PUBLIC LAW'),
         ('PRIVATE AND COMMERCIAL LAW','DEPARTMENT OF PRIVATE AND COMMERCIAL LAW'),
         ('INTERNATIONAL LAW AND SECURITY STUDIES','DEPARTMENT OF INTERNATIONAL LAW AND SECURITY STUDIES'),
         ('ACCOUNTING','DEPARTMENT OF ACCOUNTING'),
         ('FINANCE','DEPARTMENT OF FINANCE'),
         ('BUSINESS ADMINISTRATION AND MARKETING','DEPARTMENT OF BUSINESS ADMINISTRATION AND MARKETING'),
         ('INFORMATION RESOURCES MANAGEMENT','DEPARTMENT OF INFORMATION RESOURCES MANAGEMENT'),
         ('MATERNAL & CHILD HEALTH','DEPARTMENT OF MATERNAL & CHILD HEALTH'),
         ('ADULT HEALTH','DEPARTMENT OF ADULT HEALTH'),
         ('MENTAL HEALTH & PSYCHIATRY','DEPARTMENT OF MENTAL HEALTH & PSYCHIATRY'),
         ('COMMUNITY HEALTH','DEPARTMENT OF COMMUNITY HEALTH'),
         ('MEDICAL LABORATORY','DEPARTMENT OF MEDICAL LABORATORY SCIENCE'),
         ('PUBLIC HEALTH','DEPARTMENT OF PUBLIC HEALTH'),
         ('AGRICULTURE AND INDUSTRIAL TECHNOLOG','DEPARTMENT OF AGRICULTURE AND INDUSTRIAL TECHNOLOGY'),
         ('BASIC SCIENCES','DEPARTMENT OF BASIC SCIENCES'),
         ('MICROBIOLOGY','DEPARTMENT OF MICROBIOLOGY'),
         ('Economics','Department of Economics'),
         ('Mass Communication','Department of Mass Communication'),
         ('Political Science','Department of Political Science'),
         ('Social Work','Department of Social Work'),
    )
    def calculate_age(self):
        today = date.today()
        born = self.date_of_birth

        try: 
            birthday = self.date_of_birth.replace(year=today.year)
        # raised when birth date is February 29 and the current year is not a leap year
        except ValueError:
            birthday = self.date_of_birth.replace(year=today.year, day=born.day-1)

        if birthday > today:
            return today.year - born.year - 1
        else:
            return today.year - born.year
    GENDER_CHOICES = (('M','Male'),
                      ('F','Female'),)
    
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    username = models.CharField(_("username"),max_length=30, validators=[username_validation],error_messages={ "unique": _("A user with that username already exists."),},unique=True,help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),)
    first_name = models.CharField(_("first_name"),max_length=30)
    last_name = models.CharField(_("last_name"),max_length=30)
    email = models.EmailField(_("email"),unique=True, null=False, blank=False)
    matric_number = models.CharField(max_length=7, unique=True,)
    course_of_study = models.CharField(max_length=50)
    level = models.CharField(choices=undergraduate_level_choice, max_length=3)
    school = models.CharField(choices=school_choice, max_length=80)
    profile_picture = models.FileField(upload_to=profilePicture, null=True, max_length=150, blank=True)
    date_of_birth = models.DateField(max_length=8, null=True)
    age = models.IntegerField(calculate_age, null=True)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    
    is_staff = models.BooleanField(_("staff status"),default=False,help_text=_("Designates whether the user can log into this admin site."))
    is_active = models.BooleanField(_("active"),default=True,)
    
    def __str__(self):
        self.username
        return super().__str__()

    # def save(self, *args, **kwargs):
    #     self.full_clean()
    #     return super().save(*args, **kwargs)
    
    
    # ,validators=[UniqueValidator(queryset=User.objects.all())]