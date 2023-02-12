from curses.ascii import NUL
from django.db import models

# Create your models here.
class ComplainsModel(models.Model):
    
    def upload(instance, filename):
        return f"images/{filename}"
    
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
         
    COMPLAIN_STATES = (
        ('NOT SUBMITTED','NOT SUBMITTEED'),
        ('SUBMITTED','SUBMITTED'),
        ('INITIALIZED','INITIALIZED'),
        ('RESOLVED','RESOLVED'),
        ('CONFIRMED','CONFIRMED'),
        ('FAILED','FAILED'),
        ('COMPLETED', 'COMPLETED'),
        ('START','START')
    )
    
    department = models.CharField(max_length=30, choices=department_choice)
    complain = models.TextField(max_length=None)
    level = models.CharField(choices=undergraduate_level_choice,max_length=15, null=True)
    course = models.CharField(max_length=50, null=True)
    school = models.CharField(choices=school_choice, max_length=80, null=True)
    matric_number = models.CharField(max_length=7)
    name = models.CharField(max_length=100)
    complain_upload = models.FileField(upload_to=upload, null=True)
    complain_state = models.CharField(choices=COMPLAIN_STATES, default='START', null=False, max_length=20)
    

    def __str__(self):
        return self.matric_number
    
    
    
    






    # school_choice=(
        
    #     ('BENJAMIN S. CARSON (SNR) COLLEGE OF HEALTH',
    #         ('medicine','MEDICINE'),
    #         ('physiology','DEPARTMENT OF PHYSIOLOGY'),
    #         ('histology','DEPARTMENT OF HISTOLOGY'),
    #         ('community medicine','DEPARTMENT OF COMMUNITY MEDICINE'),
    #         ('nutrition and dietetics','DEPARTMENT OF NUTRITION AND DIETETICS'),
    #         ('anatomy','Department of Anatomy'),
    #         ('biochemistry','Department of Biochemistry'),
    #         ('chaemical pathology','The Department of Chemical Pathology'),
    #         ('haematoloy and immunology','DEPARTMENT OF HAEMATOLOGY AND IMMUNOLOGY'),
    #         ('micro biology','DEPARTMENT OF MEDICAL MICROBIOLOGY'),
    #      ),
        
    #     ('SCHOOL OF COMPUTING AND ENGINEERING SCIENCES',
    #      ('software engineering','DEPARTMENT OF SOFTWARE ENGINEERING'),
    #      ('computer science','DEPARTMENT OF COMPUTER SCIENCE'),
    #      ('information technology','DEPARTMENT OF INFORMATION TECHNOLOGY'),
    #      ),
        
    #     ('SCHOOL OF EDUCATION AND HUMANITIES',
    #      ('Relegious Studies','DEPARTMENT OF RELIGIOUS STUDIES'),
    #      ('Languages and Literary Studies','Department of Languages and Literary Studies'),
    #      ('History and International Studies','Department of History and International Studies'),
    #      ('Music and Creative Arts','Department of Music and Creative Arts'),
    #      ('Education','Department of Education'),
    #      ),
        
    #     ('SCHOOL OF LAW AND SECURITY STUDIES',
    #      ('JURISPRUDENCE AND PUBLIC LAW','DEPARTMENT OF JURISPRUDENCE AND PUBLIC LAW'),
    #      ('PRIVATE AND COMMERCIAL LAW','DEPARTMENT OF PRIVATE AND COMMERCIAL LAW'),
    #      ('INTERNATIONAL LAW AND SECURITY STUDIES','DEPARTMENT OF INTERNATIONAL LAW AND SECURITY STUDIES'),
    #      ),
    #     ('SCHOOL OF MANAGEMENT SCIENCES',
    #      ('ACCOUNTING','DEPARTMENT OF ACCOUNTING'),
    #      ('FINANCE','DEPARTMENT OF FINANCE'),
    #      ('BUSINESS ADMINISTRATION AND MARKETING','DEPARTMENT OF BUSINESS ADMINISTRATION AND MARKETING'),
    #      ('INFORMATION RESOURCES MANAGEMENT','DEPARTMENT OF INFORMATION RESOURCES MANAGEMENT'),
         
    #      ),
    #     ('SCHOOL OF NURSING SCIENCES',
    #      ('MATERNAL & CHILD HEALTH','DEPARTMENT OF MATERNAL & CHILD HEALTH'),
    #      ('ADULT HEALTH','DEPARTMENT OF ADULT HEALTH'),
    #      ('MENTAL HEALTH & PSYCHIATRY','DEPARTMENT OF MENTAL HEALTH & PSYCHIATRY'),
    #      ('COMMUNITY HEALTH','DEPARTMENT OF COMMUNITY HEALTH'),
    #      ),
    #     ('SCHOOL OF PUBLIC AND ALLIED HEALTH',
    #      ('MEDICAL LABORATORY','DEPARTMENT OF MEDICAL LABORATORY SCIENCE'),
    #      ('PUBLIC HEALTH','DEPARTMENT OF PUBLIC HEALTH'),
    #      ),
    #     ('SCHOOL OF SCIENCE AND TECHNOLOGY',
    #      ('AGRICULTURE AND INDUSTRIAL TECHNOLOG','DEPARTMENT OF AGRICULTURE AND INDUSTRIAL TECHNOLOGY'),
    #      ('BASIC SCIENCES','DEPARTMENT OF BASIC SCIENCES'),
    #      ('MICROBIOLOGY','DEPARTMENT OF MICROBIOLOGY'),
    #      ),
    #     ('VERONICA ADELEKE SCHOOL OF SOCIAL SCIENCES',
    #      ('Economics','Department of Economics'),
    #      ('Mass Communication','Department of Mass Communication'),
    #      ('Political Science','Department of Political Science'),
    #      ('Social Work','Department of Social Work'),
    #      ),
    # )