import email
from django.db import models
from datetime import datetime
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.dispatch import receiver
from django.forms import RegexField
from django.utils.translation import gettext_lazy as _
from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.db.models import Q
# Create your models here.
username_validation = UnicodeUsernameValidator()



class Position(models.Model):
    is_student = models.BooleanField(default=False)
    is_admin = models.BooleanField(_("is_admin"), default=False,help_text=_("Designates whether the user can log into this admin site."))
    is_staff = models.BooleanField(_("staff status"),default=False,help_text=_("Designates whether the user can log into this staff site."))
    
    def position(self):
        if self.is_student:
            return 'Student'
        elif self.is_admin:
            return 'Admin'
        elif self.is_staff:
            return 'Staff'
        else:
            return 'Other'

class UserModel(AbstractUser):
    
    def profilePicture(instance, filename):
        user = AbstractUser.username
        return f'profile_pictures/{user}/picture {filename}'
    
    
    # def calculate_age(date_of_birth):
    #     today = datetime.today()
    #     age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    #     return age
    
    GENDER_CHOICES = (('M','Male'),
                      ('F','Female'),)
    
   
    
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    username = models.CharField(_("username"),max_length=30, validators=[username_validation],error_messages={ "unique": _("A user with that username already exists."),},unique=True,help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."), default='John_doe')
    first_name = models.CharField(_("first_name"),max_length=30, default='John')
    last_name = models.CharField(_("last_name"),max_length=30, default='Doe')
    email = models.EmailField(_("email"),unique=True, blank=False, default='default@gmail.com')
    profile_picture = models.FileField(upload_to=profilePicture, null=True, max_length=150, blank=True)
    date_of_birth = models.DateField(max_length=8, null=True)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6, default='M')
    phone_number = models.CharField(default='+234 000 0000', max_length=16)
    position =models.ForeignKey(Position,max_length=10, on_delete=models.CASCADE)
    
    
    #access level
    is_active = models.BooleanField(_("active"),default=True)
    is_verified = models.BooleanField(default=False)
    
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','password',]
    
    # @property
    # def age(self):
    #     calcutate = calculate_age()
    #     return calcutate
    
    def __str__(self):
        self.username
        return super().__str__()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        username = GlobalUserModel.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)
    
    def create_staffuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Staffuser must have is_staff=True.")


        return self._create_user(username, email, password, **extra_fields)
    
    
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)

        case_insensitive_username_field = '{}__iexact'.format(UserModel.USERNAME_FIELD)
        users = UserModel._default_manager.filter(
            Q(**{case_insensitive_username_field: username}) | Q(email__iexact=username))

        # Test whether any matched user has the provided password:
        for user in users:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        if not users:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (see
            # https://code.djangoproject.com/ticket/20760)
            UserModel().set_password(password)

    
    
class StudentModel(models.Model):
        
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
    
    
    student = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    matric_number = models.CharField(max_length=7, unique=True,blank=True)
    level = models.CharField(choices=undergraduate_level_choice, max_length=3)
    course_of_study = models.CharField(max_length=50)
    school = models.CharField(choices=school_choice, max_length=80)


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
    
    staff = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    staff_number = models.CharField(max_length=12, unique=True)
    department = models.CharField(choices=department_choice,max_length=30)